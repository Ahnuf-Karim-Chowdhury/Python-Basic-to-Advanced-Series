import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

api_key = "c46b174967e2158587caaa5ad96c506c"  # Your OpenWeatherMap API key

# Function to fetch weather data
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return temp, description
    else:
        return None, None

# Function to display weather information
def show_weather(event=None):
    city = city_entry.get()
    temp, description = get_weather(city)
    
    if temp is not None:
        result_label.config(text=f"Temperature: {temp}°C\nDescription: {description.capitalize()}")
    else:
        messagebox.showerror("Error", "City not found. Please check the name and try again.")

# Set up the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")  # Set window size

# Set transparency level (0.0 is fully transparent, 1.0 is fully opaque)
app.attributes('-alpha', 0.8)  # Adjust the value to your preference

# Dark theme colors
background_color = "#1E1E1E"  # Simulate pitch black with some lighter color
foreground_color = "#FFFFFF"
input_field_color = "#4A4A4A"  # Gray.700 color
button_color = "#4A4A4A"  # Gray.700 color
button_text_color = "#FFFFFF"  # White text color

# Apply dark theme
app.configure(bg=background_color)

# Create widgets
city_label = tk.Label(app, text="Enter city:", font=('Impact', 20), bg=background_color, fg=foreground_color)
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=('Arial', 16))
city_entry.pack(pady=10, padx=20, fill=tk.X)
city_entry.configure(bg=input_field_color, fg=foreground_color, borderwidth=2, relief="solid")

search_button = tk.Button(app, text="Get Weather", command=show_weather, bg=button_color, fg=button_text_color, font=('Arial', 14))
search_button.pack(pady=10, padx=20, fill=tk.X)

result_label = tk.Label(app, text="", bg=background_color, fg=foreground_color, font=('Arial', 14))
result_label.pack(pady=20)

# Bind Enter key to the city_entry widget
city_entry.bind('<Return>', show_weather)

# Run the application
app.mainloop()
