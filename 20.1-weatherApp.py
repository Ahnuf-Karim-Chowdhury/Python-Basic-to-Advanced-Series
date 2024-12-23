import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt


class weatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name : ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)  # alt + 0176
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather APP")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

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

        self.setStyleSheet(
            """
            QLabel,QPushButton{
                font-family: ariel;
                

            }
            QLabel#city_label{
                font-size:40px;
                font-style: bold;
            }
            QLineEdit#city_input{
                font-size:30px;
            }
            QPushButton#get_weather_button{
                font-size:30px;
                font-weight:italic;
            }
            QLabel#temp_label{
                font-size: 75px;
                font-weight:italic;
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family: segoe UI emoji;
            }
            QLabel#description_label{
                font-size:40px;
            }
                           
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key="cfa5a36d999058a020675a77d36f5e11"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try :
           response= requests.get(url)
           response.raise_for_status() 
           data = response.json()

           if(data["cod"]==200):
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
                     self.display_error("Sevice Unavailable:\nServer Down!")
                case 504:
                     self.display_error("GateWay TimeOut:\nServer not Responsing!")
                case _:
                    self.display_error(f"HTTP Error Occured!\n{http_error}")
        
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error!\nPlease Check Your Internet Connection.")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error!\nThe Request Timed Iut")
        
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects!\nCheck Your URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error!\n{req_error}")


    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self,data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.16
        temp_f = (temp_k*(9/5)) - 459.67
        weather_id = data["weather"][0]["id"]
        self.temp_label.setText(f"{temp_f:.3}°F")
        weather_description = data["weather"][0]["description"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
    
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <=weather_id <=232 :
            return ("⛈")
        elif 300 <= weather_id <= 321 :
            return "🌦"
        elif 500 <= weather_id <= 531 :
            return "🌧"
        elif 600 <= weather_id <= 622 :
            return "🌨"
        elif 701 <= weather_id <= 741 :
            return "🌫"
        elif weather_id == 762 :
             return "🌋"
        elif weather_id == 771 :
             return "🎐"
        elif weather_id == 781 :
            return "🌪"
        elif weather_id == 800 :
            return "☀"
        elif 801 <= weather_id <= 804 :
            return "☁"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = weatherApp()
    weather_app.show()
    sys.exit(app.exec_())
