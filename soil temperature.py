import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('npk_environmental_data.csv')

# Randomly sample 20 data points
sampled_data = data.sample(n=20, random_state=1)

# Plotting soil temperature
plt.figure(figsize=(10, 5))
plt.plot(sampled_data['Date'], sampled_data['Temperature'], label='Soil Temperature', color='orange', marker='o')

plt.title('Soil Temperature Over Days (Random Sample)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('soil_temperature_sample.png')  # Save the figure
plt.show()