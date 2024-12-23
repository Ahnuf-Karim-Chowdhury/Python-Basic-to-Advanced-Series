import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtCore import Qt


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the user interface
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 300, 150)  # Set the window size and position

        # Set the background color of the widget
        self.setStyleSheet("background-color: #2e2e2e;")  # Dark background color

        # Create a label to display the time
        self.time_label = QLabel(self)
        self.time_label.setStyleSheet("font-size: 40px; font-weight: bold; color: #ffffff;")  # White text color
        self.time_label.setAlignment(Qt.AlignCenter)  # Center the text in the label

        # Create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)

        # Center the label in the layout
        layout.setAlignment(Qt.AlignCenter)  # Center the label within the layout
        self.setLayout(layout)

        # Set up a timer to update the clock every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Update the clock immediately
        self.update_time()

    def update_time(self):
        # Get the current time and format it
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

main()
