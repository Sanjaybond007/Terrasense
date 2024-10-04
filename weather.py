import requests
from datetime import datetime

API_KEY = '429ed4a4c99441b8a5591710240410'  # Replace with your WeatherAPI key
CITY = 'Coimbatore'  # Replace with your city name

# Function to fetch daily weather data from WeatherAPI
def get_daily_weather(city, api_key):
    # Fetch current weather
    current_url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    current_response = requests.get(current_url)
    current_data = current_response.json()

    if current_response.status_code == 200:
        print(f"Today's Weather in {city}:")
        print(f"Temperature: {current_data['current']['temp_c']}°C")
        print(f"Humidity: {current_data['current']['humidity']}%")
        print(f"Condition: {current_data['current']['condition']['text']}\n")
    else:
        print("Error fetching current weather:", current_data.get("error", {}).get("message", ""))

    # Fetch forecast for the next 7 days
    forecast_url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    if forecast_response.status_code == 200:
        print(f"7-Day Weather Forecast for {city}:\n")
        for day in forecast_data['forecast']['forecastday']:
            date = day['date']
            avg_temp = day['day']['avgtemp_c']  # Average temperature for the day
            avg_humidity = day['day']['avghumidity']  # Average humidity for the day
            condition = day['day']['condition']['text']
            print(f"Date: {date}, Avg Temp: {avg_temp}°C, Avg Humidity: {avg_humidity}%, Condition: {condition}")
    else:
        print("Error fetching forecast data:", forecast_data.get("error", {}).get("message", ""))

# Call the function
get_daily_weather(CITY, API_KEY)