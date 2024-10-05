import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
import xml.etree.ElementTree as ET

# Load the crop data from a CSV file
crop_data = pd.read_csv('npk_environmental_data_with_target.csv')

# Define a function to suggest crops based on input features
def suggest_crop(nitrogen, phosphorus, potassium, temperature, humidity, pH, soil_health):
    # Example crop suggestions based on Indian conditions
    crops = {
        'Rice': (80, 30, 30, 25, 70, 5.5),
        'Wheat': (30, 15, 15, 20, 50, 6.5),
        'Maize': (60, 20, 20, 30, 60, 6.0),
        'Pulses': (20, 10, 10, 25, 40, 6.0),
        'Cotton': (40, 20, 20, 35, 50, 7.0),
        'Sugarcane': (100, 40, 40, 30, 80, 6.5),
    }
    
    suggestions = []
    
    for crop, values in crops.items():
        if (nitrogen >= values[0] and phosphorus >= values[1] and potassium >= values[2] and 
            temperature >= values[3] and humidity >= values[4] and pH <= values[5]):
            suggestions.append(crop)
    
    return suggestions if suggestions else ["No suitable crop found"]

# Example usage
input_data = {
    'Nitrogen': crop_data['Nitrogen'].mean(),
    'Phosphorus': crop_data['Phosphorus'].mean(),
    'Potassium': crop_data['Potassium'].mean(),
    'Temperature': crop_data['Temperature'].mean(),
    'Humidity': crop_data['Humidity'].mean(),
    'pH': crop_data['pH'].mean(),
    'SoilHealth': crop_data['SoilHealth'].mean()
}

recommended_crops = suggest_crop(
    input_data['Nitrogen'],
    input_data['Phosphorus'],
    input_data['Potassium'],
    input_data['Temperature'],
    input_data['Humidity'],
    input_data['pH'],
    input_data['SoilHealth']
)

# Save the model as .bin file (dummy model for demonstration)
dummy_model = DecisionTreeClassifier() # Placeholder for an actual trained model
joblib.dump(dummy_model, 'crop_recommendation_model.bin')

# Generate XML file with recommendations
root = ET.Element("CropRecommendations")
for crop in recommended_crops:
    ET.SubElement(root, "Crop").text = crop

tree = ET.ElementTree(root)
tree.write("crop_recommendation_model.xml")

print("Model saved as .bin and .xml files.")
print("Recommended crops:", recommended_crops)
