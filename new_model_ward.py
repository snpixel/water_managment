import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_file_path = 'dataofgrpahs\ward_1_monthly_summary.csv'
data = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe to understand its structure
print(data.head())

# Calculate key metrics
data['water_distributed_l'] = data['water_distributed_l'] / data['num_people']

# Calculate the difference between distributed water and required water
data['Water_Deficit_Surplus'] = data['water_distributed_l'] - data['per_capita_usage_l']

# Plotting
plt.figure(figsize=(14, 8))

# Total water distributed per ward
plt.subplot(2, 2, 1)
plt.bar(data['ward_id'], data['water_distributed_l'], color='blue')
plt.xlabel('Ward')
plt.ylabel('Total Water Distributed (liters)')
plt.title('Total Water Distributed per Ward')
plt.xticks(rotation=90)

# Water distributed per capita per ward
plt.subplot(2, 2, 2)
plt.bar(data['ward_id'], data['water_distributed_l'], color='green')
plt.axhline(y=data['per_capita_usage_l'].mean(), color='r', linestyle='--', label='Average Per Capita Requirement')
plt.xlabel('Ward')
plt.ylabel('Water Distributed Per Capita (liters/person/day)')
plt.title('Water Distributed Per Capita per Ward')
plt.legend()
plt.xticks(rotation=90)

# Water deficit or surplus per ward
plt.subplot(2, 2, 3)
plt.bar(data['Ward'], data['Water_Deficit_Surplus'], color='orange')
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Ward')
plt.ylabel('Water Deficit/Surplus (liters/person/day)')
plt.title('Water Deficit or Surplus per Ward')
plt.xticks(rotation=90)

# Population per ward
plt.subplot(2, 2, 4)
plt.bar(data['Ward'], data['Population'], color='purple')
plt.xlabel('Ward')
plt.ylabel('Population')
plt.title('Population per Ward')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
