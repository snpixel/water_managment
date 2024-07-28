import os
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate volume based on pipe size
def calculate_volume(num_houses, pipe_size):
    # Assume volume is proportional to pipe size
    pipe_diameter = int(pipe_size.split()[0])
    return num_houses * pipe_diameter

# Function to parse CSV files and calculate total volume
def calculate_total_volume(ward_dir, constant_pipe_size=False):
    total_volume = 0
    for root, _, files in os.walk(ward_dir):
        for file in files:
            
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(root, file))
                if constant_pipe_size:
                    df['Pipe Size'] = '15 inches'  # Override with constant pipe size
                for _, row in df.iterrows():
                    num_houses = row['Number of Houses']
                    pipe_size = row['Pipe Size']
                    total_volume += calculate_volume(num_houses, pipe_size)
    return total_volume

# Directories containing the wards with variable and constant pipe sizes
base_variable_dir = 'dataofgrpahs//wards//ward_'
base_constant_dir = 'dataofgrpahs//old_wards//ward_'

# Initialize lists to hold volumes
variable_volumes = []
constant_volumes = []

# Loop through all 84 wards
for i in range(1, 85):
    ward_number = f'{i}'  # Format ward number with leading zero if necessary
    variable_pipe_size_dir = base_variable_dir + ward_number
    constant_pipe_size_dir = base_constant_dir + ward_number
    
    # Calculate volumes for the current ward
    variable_total_volume = calculate_total_volume(variable_pipe_size_dir)
    constant_total_volume = calculate_total_volume(constant_pipe_size_dir, constant_pipe_size=True)
    
    # Append volumes to lists
    variable_volumes.append(variable_total_volume)
    
    constant_volumes.append(constant_total_volume)

# Data for plotting
ward_numbers = [f'Ward {i}' for i in range(1, 85)]

# Create bar graph
plt.figure(figsize=(12, 8))
width = 0.35  # Width of bars
x = range(len(ward_numbers))  # x locations for the groups

plt.bar([p - width/2 for p in x], variable_volumes, width=width, label='Variable Pipe Size Wards', color='blue')
plt.bar([p + width/2 for p in x], constant_volumes, width=width, label='Constant Pipe Size Wards', color='red')

plt.xlabel('Ward')
plt.ylabel('Total Volume')
plt.title('Total Volume Comparison: Variable vs Constant Pipe Size Wards')
plt.xticks(x, ward_numbers, rotation=90)  # Rotate ward numbers for readability
plt.legend()
plt.tight_layout()
plt.show()
