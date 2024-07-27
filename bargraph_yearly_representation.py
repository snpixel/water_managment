import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the ward names and file paths
wards = [f"ward_{i}" for i in range(1,86)]
file_paths = [f'dataofgrpahs/{ward.lower()}_yearly_summary.csv' for ward in wards]

# Initialize lists to store total water requirement and supply
total_requirements = []
total_supplies = []

# Read data from each CSV file and calculate totals
for file_path in file_paths:
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        total_requirement = (df['num_people'] * df['per_capita_usage_l']).sum()
        total_supply = df['water_distributed_l'].sum()
        total_requirements.append(total_requirement)
        total_supplies.append(total_supply)
    else:
        print(f"File {file_path} not found.")
        total_requirements.append(0)
        total_supplies.append(0)

# Create a DataFrame for plotting
plot_df = pd.DataFrame({
    'Ward Number': [str(i+1) for i in range(len(wards))],
    'Total Requirement': total_requirements,
    'Total Supply': total_supplies
})

# Plot the data
plt.figure(figsize=(20, 12))  # Increase the figure size

# Define bar width and positions
bar_width = 0.35
index = range(len(wards))
spacing = 1.5  # Increase the distance between groups

# Create side-by-side bar plots with increased distance between wards
for i in range(len(wards)):
    plt.bar(index[i] - bar_width/2, plot_df.loc[i, 'Total Requirement'], width=bar_width, label='Total Requirement' if i == 0 else "", color='blue')
    plt.bar(index[i] + bar_width/2, plot_df.loc[i, 'Total Supply'], width=bar_width, label='Total Supply' if i == 0 else "", color='orange')

# Add labels, title, and legend
plt.xlabel('Ward Number')
plt.ylabel('Volume (L)')
plt.title('Comparison of Total Water Requirement and Supply by Ward')
plt.xticks(index, plot_df['Ward Number'], rotation=90, fontsize=8)  # Rotate labels and reduce font size
plt.legend()

# Adjust layout and spacing
plt.tight_layout()
plt.subplots_adjust(bottom=0.2, left=0.1, right=0.9)

# Save the plot as a PNG file
plt.savefig('ward_water_comparison.png')

# Display the plot
plt.show()