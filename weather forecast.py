import tkinter as tk
import requests

class WeatherForecastApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast")

        self.location_label = tk.Label(root, text="Enter City or Zip Code:")
        self.location_label.grid(row=0, column=0, padx=10, pady=10)

        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=1, columnspan=2, padx=10, pady=10)

        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.grid(row=2, columnspan=2, padx=10, pady=10)

    def get_weather(self):
        try:
            location = self.location_entry.get()
            if not location:
                self.weather_info_label.config(text="Please enter a location.")
                return

            api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_description = data["weather"][0]["description"].capitalize()
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]

                weather_info = f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
                self.weather_info_label.config(text=weather_info)
            else:
                self.weather_info_label.config(text="Location not found. Please enter a valid location.")
        except Exception as e:
            self.weather_info_label.config(text=f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = WeatherForecastApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
