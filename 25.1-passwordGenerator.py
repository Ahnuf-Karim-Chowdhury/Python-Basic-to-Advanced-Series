from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
)
from PyQt5.QtCore import Qt, QPoint
import sys
import random

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(40)

        self.title_label = QLabel("Password Generator", self)
        self.title_label.setStyleSheet("color: white; font-size: 20px;")
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
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
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_start_position = event.globalPos() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = event.globalPos() - self.drag_start_position
            self.parent().move(new_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            event.accept()

    def close_window(self):
        self.parent().close()

    def minimize_window(self):
        self.parent().showMinimized()

    def toggle_theme(self):
        self.parent().toggle_theme()

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.95)
        self.is_dark_mode = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")
        self.resize(500, 300)

        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        self.password_label = QLabel("Generated Password:", self)
        self.password_display = QLineEdit(self)
        self.password_display.setReadOnly(True)
        self.generate_button = QPushButton("Generate Password", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_display)
        vbox.setSpacing(20)
        vbox.addWidget(self.generate_button)
        vbox.setContentsMargins(50, 50, 50, 50)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_display.setAlignment(Qt.AlignCenter)

        self.password_label.setObjectName("password_label")
        self.password_display.setObjectName("password_display")
        self.generate_button.setObjectName("generate_button")

        self.apply_dark_theme()

        self.generate_button.clicked.connect(self.generate_password)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
            }
            QLabel, QLineEdit, QPushButton {
                color: #FFFFFF;
                font-family: Arial;
            }
            QLabel#password_label {
                font-size: 25px;
                font-weight: bold;
            }
            QLineEdit#password_display {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 20px;
                border: 2px solid #FFFFFF;
            }
            QPushButton#generate_button {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 20px;
                border: none;
            }
            QPushButton#generate_button:hover {
                background-color: #6A6A6A;
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌙")

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
            }
            QLabel, QLineEdit, QPushButton {
                color: #000000;
                font-family: Arial;
            }
            QLabel#password_label {
                font-size: 25px;
                font-weight: bold;
            }
            QLineEdit#password_display {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 20px;
                border: 2px solid #000000;
            }
            QPushButton#generate_button {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 20px;
                border: none;
            }
            QPushButton#generate_button:hover {
                background-color: #AAAAAA;
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌞")

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
        self.is_dark_mode = not self.is_dark_mode

    def generate_password(self):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?"
        password = ''.join(random.choice(characters) for _ in range(12))
        self.password_display.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
