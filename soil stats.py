import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')

# Function to fetch weather data
def fetch_weather(api_key, city):
    # Current weather
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    current_weather = requests.get(current_weather_url).json()

    # Forecast for the next 5 days (including today)
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    forecast_data = requests.get(forecast_url).json()

    return current_weather, forecast_data

# Function to display weather data for specific dates
def display_weather(api_key, city):
    current_weather, forecast_data = fetch_weather(api_key, city)

    # Display current weather
    print("Current Weather:")
    print(f"Temperature: {current_weather['main']['temp']}°C")
    print(f"Humidity: {current_weather['main']['humidity']}%")
    print(f"Weather: {current_weather['weather'][0]['description']}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Get today's date
    today = datetime.now().date()
    
    # Define specific dates to display
    specific_dates = [
        today - timedelta(days=2),  # October 2nd
        today - timedelta(days=1),  # October 3rd
        today + timedelta(days=1),  # October 5th
        today + timedelta(days=2)   # October 6th
    ]

    # Initialize a dictionary to hold average weather data for specific dates
    average_weather = {date: {'temp': [], 'humidity': []} for date in specific_dates}

    # Collect weather data for specific dates
    for entry in forecast_data['list']:
        forecast_date = datetime.fromtimestamp(entry['dt']).date()
        
        if forecast_date in specific_dates:
            average_weather[forecast_date]['temp'].append(entry['main']['temp'])
            average_weather[forecast_date]['humidity'].append(entry['main']['humidity'])

    # Calculate and display average weather for each specified date
    print("Average Weather for Specific Dates:")
    
    for date in specific_dates:
        if average_weather[date]['temp']:  # Check if there are any recorded temperatures for the date
            avg_temp = sum(average_weather[date]['temp']) / len(average_weather[date]['temp'])
            avg_humidity = sum(average_weather[date]['humidity']) / len(average_weather[date]['humidity'])
            print(f"Date: {date}")
            print(f"Average Temperature: {avg_temp:.2f}°C")
            print(f"Average Humidity: {avg_humidity:.2f}%")
            print(f"Weather: {forecast_data['list'][0]['weather'][0]['description']}\n")  # Using the first entry's description

# Load the crop recommendation dataset and sample 200 random entries
def load_crop_data():
    data = pd.read_csv("Crop_recommendation.csv")
    
    # Sample 200 random rows from the dataset
    sampled_data = data.sample(n=200, random_state=1)  # random_state for reproducibility
    return sampled_data

# Display crop statistics and plots
def display_crop_statistics(data):
    print("Basic Crop Statistics:")
    print(data.describe())
    
    # Display the most common crop
    most_common_crop = data['label'].value_counts().idxmax()
    print(f"Most Common Crop: {most_common_crop}\n")

def plot_soil_health(data):
    plt.figure(figsize=(12, 6))
    
    sns.boxplot(data=data[['N', 'P', 'K', 'ph']], palette="Set2")
    
    plt.title('Soil Nutrient Levels', fontsize=16)
    plt.xlabel('Nutrients', fontsize=14)
    plt.ylabel('Values', fontsize=14)
    
    plt.grid(axis='y')
    
    plt.show()

def plot_weather_impact(data):
    plt.figure(figsize=(12, 6))
    
    sns.scatterplot(x='temperature', y='rainfall', hue='label', data=data, palette="Set1", s=100)
    
    plt.title('Temperature vs Rainfall by Crop Type', fontsize=16)
    plt.xlabel('Temperature (°C)', fontsize=14)
    plt.ylabel('Rainfall (mm)', fontsize=14)
    
    plt.legend(title='Crop Type')
    
    plt.grid(True)
    
    plt.show()

def plot_crop_suggestions(data):
    crop_counts = data['label'].value_counts()
    
    plt.figure(figsize=(12, 6))
    
    crop_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Crop Suggestions Based on Soil Health', fontsize=16)
    plt.xlabel('Crop Type', fontsize=14)
    plt.ylabel('Count', fontsize=14)

    plt.xticks(rotation=45)
    plt.grid(axis='y')
   
    plt.show()

# Main function to run the analysis and display both weather and crop statistics
def main():
   api_key = "218d4c21db04161e387d87a51d72c43b"  # Your actual API key here
   city = "Coimbatore"  # City name as a string
    
   # Display weather information
   display_weather(api_key, city)
    
   # Load and display crop data statistics and plots
   crop_data = load_crop_data()
   display_crop_statistics(crop_data)

if __name__ == "__main__":
   main()