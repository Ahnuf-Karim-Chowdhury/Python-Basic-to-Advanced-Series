from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow
)
from PyQt5.QtCore import Qt
import sys
import requests

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(40)

        self.title_label = QLabel("Weather APP", self)
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

    def close_window(self):
        self.parent().close()

    def minimize_window(self):
        self.parent().showMinimized()

    def toggle_theme(self):
        self.parent().toggle_theme()  # Notify parent to toggle theme

class weatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.8)
        self.is_dark_mode = True  # Track current theme mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather APP")
        self.resize(700, 500)

        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        self.city_label = QLabel("Enter City Name : ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.setSpacing(15)
        vbox.addWidget(self.get_weather_button)
        vbox.setSpacing(40)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Apply dark theme initially
        self.apply_dark_theme()

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
            }
            QLabel, QLineEdit, QPushButton {
                color: #FFFFFF;
                font-family: Arial;
            }
            QLabel#city_label {
                font-size: 50px;
                font-family: Impact;
            }
            QLineEdit#city_input {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 30px;
                border: 2px solid #FFFFFF;
            }
            QPushButton#get_weather_button {
                background-color: #4A4A4A;
                color: #FFFFFF;
                font-size: 40px;
                border: none;
            }
            QPushButton#get_weather_button:hover {
                background-color: #6A6A6A;
            }
            QLabel#temp_label {
                font-size: 75px;
                font-weight: italic;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 30px;
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
            QLabel#city_label {
                font-size: 50px;
                font-family: Impact;
            }
            QLineEdit#city_input {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 30px;
                border: 2px solid #000000;
            }
            QPushButton#get_weather_button {
                background-color: #CCCCCC;
                color: #000000;
                font-size: 40px;
                border: none;
            }
            QPushButton#get_weather_button:hover {
                background-color: #AAAAAA;
            }
            QLabel#temp_label {
                font-size: 75px;
                font-weight: italic;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 20px;
            }
        """)
        self.custom_title_bar.toggle_button.setText("🌞")  # Light mode icon

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
        self.is_dark_mode = not self.is_dark_mode

    def get_weather(self):
        api_key = "cfa5a36d999058a020675a77d36f5e11"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Invalid Request:\nCheck Your Input!")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API KEY!")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied!")
                case 404:
                    self.display_error("Not Found:\nCity Not Found!")
                case 500:
                    self.display_error("Server Error:\nPlease Try Again Later!")
                case 502:
                    self.display_error("Bad GateWay:\nInvalid Server Response!")
                case 503:
                    self.display_error("Service Unavailable:\nServer Down!")
                case 504:
                    self.display_error("GateWay TimeOut:\nServer not Responding!")
                case _:
                    self.display_error(f"HTTP Error Occurred!\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error!\nPlease Check Your Internet Connection.")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error!\nThe Request Timed Out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects!\nCheck Your URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error!\n{req_error}")

    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temp_k = data["main"]["temp"]
        temp_f = (temp_k * (9 / 5)) - 459.67
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"]

        self.temp_label.setText(f"{temp_f:.2f} °F")
        self.description_label.setText(f"{description}")

        weather_icons = {
            (200, 232): "⛈️",  # Thunderstorm
            (300, 321): "🌦️",  # Drizzle
            (500, 531): "🌧️",  # Rain
            (600, 622): "🌨️",  # Snow
            (700, 781): "🌫️",  # Atmosphere
            (800, 800): "☀️",  # Clear
            (801, 804): "☁️"   # Clouds
        }

        emoji = next((emoji for (start, end), emoji in weather_icons.items() if start <= weather_id <= end), "❓")
        self.emoji_label.setText(emoji)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = weatherApp()
    ex.show()
    sys.exit(app.exec_())
