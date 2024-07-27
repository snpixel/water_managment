import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('water_managment\dataofgrpahs\data_csv_wards\ward_1_monthly_summary.csv')

# Calculate the average water requirement
df['Average_Requirement'] = df['num_people'] * df['per_capita_usage_l']

# Plot the data
plt.figure(figsize=(12, 6))

# Plot water distributed
plt.plot(df['date'], df['water_distributed_l'], label='Water Distributed', marker='o')

# Plot average water requirement
plt.plot(df['date'], df['Average_Requirement'], label='Average Requirement', marker='x')

# Adding titles and labels
plt.title('Comparison of Water Supply and Average Requirement')
plt.xlabel('Months')
plt.ylabel('Volume (L)')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('water_supply_vs_requirement.png')

# Display the plot
plt.show()
