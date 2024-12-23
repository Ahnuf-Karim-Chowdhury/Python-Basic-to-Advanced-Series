import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPalette, QColor

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0)  # Initialize self.time here
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 400, 200)  # Change width and height here

        # Set dark background
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(palette)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Stopwatch display
        self.display = QLabel()
        self.display.setStyleSheet(
            "font-size: 40px; color: white;"
        )  # Adjust font size for larger window
        self.display.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.display)

        # Start/Stop button
        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.toggleTimer)
        self.layout.addWidget(self.start_stop_button)

        # Initialize stopwatch display
        self.updateDisplay()

    def updateTime(self):
        self.time = self.time.addSecs(1)
        self.updateDisplay()

    def updateDisplay(self):
        if self.time:  # Check if self.time is initialized
            self.display.setText(self.time.toString("HH:mm:ss"))

    def toggleTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(1000)  # Update every second
            self.start_stop_button.setText("Stop")

def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

main()
