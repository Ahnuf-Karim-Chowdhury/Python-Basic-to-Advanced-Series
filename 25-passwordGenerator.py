import sys
import string
import secrets
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class StrongPasswordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window Title and Geometry
        self.setWindowTitle('Strong Password Generator')
        self.setGeometry(100, 100, 400, 250)

        # Label for password input
        self.input_label = QLabel('Enter your password or string:', self)
        self.input_label.setFont(QFont('Arial', 12))

        # Input field for the string
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter any combination of letters, numbers, symbols')
        self.input_field.setFont(QFont('Arial', 12))

        # Connect pressing 'Enter' in the input field to the generate_strong_password method
        self.input_field.returnPressed.connect(self.generate_strong_password)

        # Generate button
        self.generate_button = QPushButton('Generate Strong Password', self)
        self.generate_button.setFont(QFont('Arial', 12))
        self.generate_button.clicked.connect(self.generate_strong_password)

        # Label to display the generated strong password
        self.password_label = QLabel('', self)
        self.password_label.setFont(QFont('Arial', 12))
        self.password_label.setWordWrap(True)
        self.password_label.setStyleSheet('QLabel { background-color: #e6e6e6; border: 1px solid #bfbfbf; padding: 5px; }')

        # Make the password label selectable by mouse and keyboard
        self.password_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.TextSelectableByKeyboard
        )

        # Center-align the password label
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout setup
        layout = QVBoxLayout()

        # Add input, button, and password label to layout
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.generate_button)

        # Center the password label by using a centered HBoxLayout
        password_layout = QHBoxLayout()
        password_layout.addStretch(1)
        password_layout.addWidget(self.password_label)
        password_layout.addStretch(1)

        # Add the password label layout to the main layout
        layout.addLayout(password_layout)

        # Set the layout
        self.setLayout(layout)

    def generate_strong_password(self):
        # Get the input string from the user
        input_string = self.input_field.text()

        if not input_string:
            self.password_label.setText("Please enter a valid string to strengthen.")
            return

        # Strengthen the password
        strong_password = self.strengthen_password(input_string)

        # Display the strong password in the label (centered and selectable)
        self.password_label.setText(f"Your strong password is:\n{strong_password}")

    def strengthen_password(self, input_string):
        # Ensure the password has at least 12 characters
        min_length = 12
        characters = list(input_string)

        # Add random characters until the password is at least 12 characters long
        all_characters = string.ascii_letters + string.digits + string.punctuation
        while len(characters) < min_length:
            characters.append(secrets.choice(all_characters))

        # Ensure there is at least one uppercase, one lowercase, one digit, and one symbol
        if not any(c.islower() for c in characters):
            characters.append(secrets.choice(string.ascii_lowercase))
        if not any(c.isupper() for c in characters):
            characters.append(secrets.choice(string.ascii_uppercase))
        if not any(c.isdigit() for c in characters):
            characters.append(secrets.choice(string.digits))
        if not any(c in string.punctuation for c in characters):
            characters.append(secrets.choice(string.punctuation))

        # Shuffle the characters to make the password unpredictable
        random.shuffle(characters)

        # Join the characters to form the final strong password
        strong_password = ''.join(characters)

        return strong_password


def main():
    app = QApplication(sys.argv)
    window = StrongPasswordApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
