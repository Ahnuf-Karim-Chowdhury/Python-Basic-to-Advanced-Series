import sys
import string
import secrets
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QPoint


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(40)

        self.title_label = QLabel("Strong Password Generator", self)
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

        self.toggle_button = QPushButton("🌙", self)  # Default icon for dark mode
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
            self.drag_start_position = event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = event.globalPosition().toPoint() - self.drag_start_position
            self.parent().move(new_position)
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


class StrongPasswordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        self.is_dark_mode = True  # Track current theme mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Strong Password Generator")
        self.resize(700, 500)

        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        # Main UI components
        self.input_label = QLabel('Enter your password or string:', self)
        self.input_field = QLineEdit(self)
        self.generate_button = QPushButton('Generate Strong Password', self)
        self.password_label = QLabel('', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_field)
        vbox.setSpacing(15)
        vbox.addWidget(self.generate_button)
        vbox.setSpacing(40)
        vbox.addWidget(self.password_label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        # Set alignment for all widgets
        self.input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set object names for styling
        self.input_label.setObjectName("input_label")
        self.input_field.setObjectName("input_field")
        self.generate_button.setObjectName("generate_button")
        self.password_label.setObjectName("password_label")

        # Connect buttons
        self.generate_button.clicked.connect(self.generate_strong_password)
        self.input_field.returnPressed.connect(self.generate_strong_password)

        # Apply dark theme initially
        self.apply_dark_theme()

    def generate_strong_password(self):
        # Get the input string from the user
        input_string = self.input_field.text()

        if not input_string:
            self.password_label.setText("Please enter a valid string to strengthen.")
            return

        # Strengthen the password
        strong_password = self.strengthen_password(input_string)

        # Display the strong password
        self.password_label.setText(f"Your strong password is:\n{strong_password}")

    def strengthen_password(self, input_string):
        min_length = 12
        characters = list(input_string)
        all_characters = string.ascii_letters + string.digits + string.punctuation

        while len(characters) < min_length:
            characters.append(secrets.choice(all_characters))

        if not any(c.islower() for c in characters):
            characters.append(secrets.choice(string.ascii_lowercase))
        if not any(c.isupper() for c in characters):
            characters.append(secrets.choice(string.ascii_uppercase))
        if not any(c.isdigit() for c in characters):
            characters.append(secrets.choice(string.digits))
        if not any(c in string.punctuation for c in characters):
            characters.append(secrets.choice(string.punctuation))

        random.shuffle(characters)
        return ''.join(characters)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
            }
            QLabel, QLineEdit, QPushButton {
                color: #FFFFFF;
                font-family: Arial;
            }
            QLabel#input_label {
                font-size: 30px;
            }
            QLineEdit#input_field {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 20px;
                border: 2px solid #FFFFFF;
            }
            QPushButton#generate_button {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 30px;
                border: none;
            }
            QPushButton#generate_button:hover {
                background-color: #6A6A6A;
            }
            QLabel#password_label {
                font-size: 20px;
                background-color: #e6e6e6;
                color: #000000;
                padding: 10px;
                border: 1px solid #bfbfbf;
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌙")  # Dark mode icon

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
            }
            QLabel, QLineEdit, QPushButton {
                color: #000000;
                font-family: Arial;
            }
            QLabel#input_label {
                font-size: 30px;
            }
            QLineEdit#input_field {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 20px;
                border: 2px solid #000000;
            }
            QPushButton#generate_button {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 30px;
                border: none;
            }
            QPushButton#generate_button:hover {
                background-color: #AAAAAA;
            }
            QLabel#password_label {
                font-size: 20px;
                background-color: #e6e6e6;
                color: #000000;
                padding: 10px;
                border: 1px solid #bfbfbf;
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌞")  # Light mode icon

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
        self.is_dark_mode = not self.is_dark_mode


def main():
    app = QApplication(sys.argv)
    window = StrongPasswordApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
