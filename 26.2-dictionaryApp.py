from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow
)
from PyQt6.QtCore import Qt, QPoint
import sys
import requests

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")  # Semi-transparent black
        self.setFixedHeight(40)

        self.title_label = QLabel("Dictionary App", self)
        self.title_label.setStyleSheet("color: white; font-size: 20px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.title_label.setFixedSize(620, 40)

        self.close_button = QPushButton("X", self)
        self.close_button.setStyleSheet("background-color: red; color: white; border: none;")
        self.close_button.setFixedSize(40, 40)
        self.close_button.clicked.connect(self.close_window)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.setStyleSheet("background-color: gray; color: white; border: none;")
        self.minimize_button.setFixedSize(40, 40)
        self.minimize_button.clicked.connect(self.minimize_window)

        self.toggle_button = QPushButton("🌙", self)
        self.toggle_button.setStyleSheet("background-color: gray; color: white; border: none;")
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.clicked.connect(self.toggle_theme)

        hbox = QHBoxLayout()
        hbox.addWidget(self.title_label)
        hbox.addStretch()
        hbox.addWidget(self.toggle_button)
        hbox.addWidget(self.minimize_button)
        hbox.addWidget(self.close_button)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hbox)

        self.is_dragging = False
        self.drag_start_position = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            self.drag_start_position = event.globalPosition() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = event.globalPosition() - self.drag_start_position
            self.parent().move(new_position.toPoint())
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            event.accept()

    def close_window(self):
        self.parent().close()

    def minimize_window(self):
        self.parent().showMinimized()

    def toggle_theme(self):
        self.parent().toggle_theme()

class DictionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(700, 400)
        self.is_dark_mode = True  # Start in dark mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dictionary App")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        self.word_label = QLabel("Enter a word: ", self)
        self.word_input = QLineEdit(self)
        self.lookup_button = QPushButton("Look Up", self)
        self.meaning_label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.word_label)
        vbox.addWidget(self.word_input)
        vbox.addWidget(self.lookup_button)
        vbox.addWidget(self.meaning_label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meaning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meaning_label.setWordWrap(True)

        self.lookup_button.clicked.connect(self.lookup_word)
        self.word_input.returnPressed.connect(self.lookup_word)

        # Apply dark theme initially
        self.apply_dark_theme()

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
        self.is_dark_mode = not self.is_dark_mode

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(30, 30, 30, 200);  /* Semi-transparent dark background */
            }
            QLabel, QLineEdit, QPushButton {
                color: #FFFFFF;
                font-family: Arial;
            }
            QLabel {
                font-size: 20px;
            }
            QLineEdit {
                background-color: rgba(74, 74, 74, 200); /* Semi-transparent input */
                color: #FFFFFF;
                font-size: 20px;
                border: 2px solid #FFFFFF;
            }
            QPushButton {
                background-color: rgba(74, 74, 74, 200); /* Semi-transparent button */
                color: #FFFFFF;
                font-size: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(106, 106, 106, 200); /* Semi-transparent hover */
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌙")  # Dark mode icon

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 200); /* Semi-transparent light background */
            }
            QLabel, QLineEdit, QPushButton {
                color: #000000;
                font-family: Arial;
            }
            QLabel {
                font-size: 20px;
            }
            QLineEdit {
                background-color: rgba(204, 204, 204, 200); /* Semi-transparent input */
                color: #000000;
                font-size: 20px;
                border: 2px solid #000000;
            }
            QPushButton {
                background-color: rgba(204, 204, 204, 200); /* Semi-transparent button */
                color: #000000;
                font-size: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(170, 170, 170, 200); /* Semi-transparent hover */
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌞")  # Light mode icon

    def lookup_word(self):
        word = self.word_input.text().strip()
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        if response.status_code == 200:
            data = response.json()
            meanings_text = ""

            for meaning in data[0]['meanings']:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                
                # Constructing the formatted output
                for definition in definitions:
                    meanings_text += f"{part_of_speech.capitalize()}: {definition['definition']}\n"

            self.meaning_label.setText(meanings_text.strip())
        else:
            self.meaning_label.setText(f"The word '{word}' was not found in the dictionary.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec())
