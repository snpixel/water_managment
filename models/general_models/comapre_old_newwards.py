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
variable_pipe_size_dir = 'dataofgrpahs//wards//ward_1'
constant_pipe_size_dir = 'dataofgrpahs//old_wards//ward_1'

# Calculate total volumes

variable_total_volume = calculate_total_volume(variable_pipe_size_dir)
constant_total_volume = calculate_total_volume(constant_pipe_size_dir, constant_pipe_size=True)

# Data for plotting
labels = ['Variable Pipe Size Wards(New_layout)', 'Constant Pipe Size Wards(old_layout)']
volumes = [variable_total_volume, constant_total_volume]

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
variable_pipe_size_dir = 'dataofgrpahs//wards//ward_1'
constant_pipe_size_dir = 'dataofgrpahs//old_wards//ward_1'

# Calculate total volumes

variable_total_volume = calculate_total_volume(variable_pipe_size_dir)
constant_total_volume = calculate_total_volume(constant_pipe_size_dir, constant_pipe_size=True)

# Data for plotting
labels = ['Variable Pipe Size Wards(New_layout)', 'Constant Pipe Size Wards(old_layout)']
volumes = [variable_total_volume, constant_total_volume]

# Create bar graph
plt.figure(figsize=(10, 6))
plt.bar(labels, volumes, color=['blue', 'green'])
plt.xlabel('Ward Type')
plt.ylabel('Total Volume')
plt.title('Total Volume Comparison: Variable vs Constant Pipe Size Wards')
plt.show()
