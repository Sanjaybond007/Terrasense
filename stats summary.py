import pandas as pd

# Load dataset from the provided CSV file
data = pd.read_csv("npk_environmental_data.csv")

# Randomly sample 20 data points
sampled_data = data.sample(n=20, random_state=1)

# Calculate average values for soil nutrients and other parameters
avg_nitrogen = sampled_data['Nitrogen'].mean()
avg_phosphorus = sampled_data['Phosphorus'].mean()
avg_potassium = sampled_data['Potassium'].mean()
avg_temperature = sampled_data['Temperature'].mean()
avg_humidity = sampled_data['Humidity'].mean()
avg_ph = sampled_data['pH'].mean()

# Function to generate a response based on average soil health parameters
def generate_response(nitrogen, phosphorus, potassium, temperature, humidity, ph):
    response = f"Based on the average soil health parameters over the last 20 days:\n"
    response += f"- Average Nitrogen: {nitrogen:.2f} ppm\n"
    response += f"- Average Phosphorus: {phosphorus:.2f} ppm\n"
    response += f"- Average Potassium: {potassium:.2f} ppm\n"
    response += f"- Average Temperature: {temperature:.2f}°C\n"
    response += f"- Average Humidity: {humidity:.2f}%\n"
    response += f"- Average pH Level: {ph:.2f}\n\n"

    # Generate crop suggestions based on NPK values
    if nitrogen < 30:
        response += "The nitrogen level is low; consider planting legumes to improve nitrogen content.\n"
    elif nitrogen < 60:
        response += "The nitrogen level is moderate; suitable for cereals like wheat and barley.\n"
    else:
        response += "High nitrogen levels are ideal for leafy greens and some root vegetables.\n"

    if phosphorus < 40:
        response += "Phosphorus levels are low; consider adding phosphorus-rich fertilizers.\n"
    elif phosphorus < 70:
        response += "Moderate phosphorus levels are suitable for most vegetables.\n"
    else:
        response += "High phosphorus levels can benefit fruit-bearing plants.\n"

    if potassium < 40:
        response += "Potassium levels are low; consider adding potassium-rich fertilizers.\n"
    elif potassium < 70:
        response += "Adequate potassium levels support healthy plant growth.\n"
    else:
        response += "High potassium levels are beneficial for root crops and fruits.\n"

    # Temperature and humidity considerations
    if temperature > 30 and humidity > 60:
        response += "The warm and humid conditions are suitable for tropical crops like rice and sugarcane.\n"
    elif temperature < 20:
        response += "Cooler temperatures may require crops that thrive in such conditions, like certain leafy greens.\n"
    
    # pH level considerations
    if ph < 6.0:
        response += "The soil is acidic; consider liming to raise the pH for better nutrient availability.\n"
    elif ph > 7.5:
        response += "The soil is alkaline; monitor nutrient availability closely as some nutrients may become deficient.\n"

    return response

# Generate a summary based on average values
summary_response = generate_response(avg_nitrogen, avg_phosphorus, avg_potassium,
                                     avg_temperature, avg_humidity, avg_ph)

# Print the summary
print(summary_response)