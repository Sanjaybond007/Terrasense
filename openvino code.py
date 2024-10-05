
# Import necessary libraries
import pandas as pd
import numpy as np
from openvino.runtime import Core

# Upload your CSV file
from google.colab import files
uploaded = files.upload()

# Load the CSV file with soil data
data = pd.read_csv('npk_environmental_data.csv')  # Update with your actual CSV file name

# Load OpenVINO model (assuming you have uploaded .xml and .bin files)
model_xml = 'soil_health_model.xml'  # Update with your model path
model_bin = 'soil_health_model.bin'   # Update with your model path

# Initialize OpenVINO runtime
ie = Core()
model = ie.read_model(model=model_xml, weights=model_bin)
compiled_model = ie.compile_model(model=model, device_name="CPU")

# Prepare input data for inference
features = data[['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH']].values

# Perform inference
results = compiled_model.infer({model.inputs[0]: features})

# Extract predictions (assuming output is a one-dimensional array of class probabilities)
predictions = np.argmax(results[model.outputs[0]], axis=1)

# Add predictions to DataFrame
data['PredictedSoilHealth'] = predictions

# Map numerical predictions back to categorical values if needed
data['PredictedSoilHealth'] = data['PredictedSoilHealth'].map({2: 'Good', 1: 'Moderate', 0: 'Poor'})

# Display results
print(data[['Date', 'PredictedSoilHealth']])
