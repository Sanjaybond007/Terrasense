import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('npk_environmental_data.csv')

# Randomly sample 20 data points
sampled_data = data.sample(n=20, random_state=1)

# Plotting pH levels
plt.figure(figsize=(10, 5))
plt.plot(sampled_data['Date'], sampled_data['pH'], label='pH Level', color='green', marker='o')

plt.title('pH Level Over Days (Random Sample)')
plt.xlabel('Date')
plt.ylabel('pH Level')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('ph_level_sample.png')  # Save the figure
plt.show()