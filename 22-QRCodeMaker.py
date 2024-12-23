from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
)
from PyQt5.QtCore import Qt, QPoint
import sys
import qrcode
import os
import svgwrite

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(40)

        self.title_label = QLabel("QR Code Generator", self)
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

        hbox = QHBoxLayout()
        hbox.addWidget(self.title_label)
        hbox.addStretch()
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


class QRCodeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QR Code Generator")
        self.resize(700, 500)

        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        self.label = QLabel("Enter text or URL: ", self)
        self.input_field = QLineEdit(self)
        self.generate_button = QPushButton("Generate QR Code", self)
        self.status_label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.input_field)
        vbox.setSpacing(15)
        vbox.addWidget(self.generate_button)
        vbox.setSpacing(40)
        vbox.addWidget(self.status_label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.label.setAlignment(Qt.AlignCenter)
        self.input_field.setAlignment(Qt.AlignCenter)
        self.status_label.setAlignment(Qt.AlignCenter)

        # Set object names for styling
        self.label.setObjectName("label")
        self.input_field.setObjectName("input_field")
        self.generate_button.setObjectName("generate_button")
        self.status_label.setObjectName("status_label")

        # Apply dark theme
        self.apply_dark_theme()

        # Connect button click
        self.generate_button.clicked.connect(self.generate_qr_code)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
            }
            QLabel, QLineEdit, QPushButton {
                color: #FFFFFF;
                font-family: Arial;
            }
            QLabel#label {
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
            QLabel#status_label {
                font-size: 20px;
            }
        """)

    def generate_qr_code(self):
        text = self.input_field.text()
        if not text:
            self.status_label.setText("Please enter some text or a URL.")
            return

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Save as PNG
        img = qr.make_image(fill='black', back_color='white')
        img_folder = "qrcodes"
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)
        png_path = os.path.join(img_folder, "qrcode.png")
        img.save(png_path)

        # Save as SVG
        svg_path = os.path.join(img_folder, "qrcode.svg")
        dwg = svgwrite.Drawing(svg_path, profile='tiny')
        qr_matrix = qr.get_matrix()
        for y, row in enumerate(qr_matrix):
            for x, val in enumerate(row):
                if val:
                    dwg.add(dwg.rect(insert=(x * 10, y * 10), size=(10, 10), fill='black'))
        dwg.save()

        # Update status
        self.status_label.setText(f"QR Code generated and saved as PNG and SVG in {img_folder}.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())
