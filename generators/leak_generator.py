import csv
import random

# Function to generate synthetic data
def generate_synthetic_data_with_leaks(num_records, leak_ratio=0.1):
    data = []
    for _ in range(num_records):
        # Generate random flow rates for the big pipe and tank inflow
        big_pipe_flow_rate = round(random.uniform(0.01, 0.1), 3)  # m³/s
        time_period = random.randint(300, 3600)  # 5 minutes to 1 hour
        tank_volume = random.randint(100, 1000)  # m³

        # Determine if this record should simulate a leak
        if random.random() < leak_ratio:
            # Simulate a leak by making the tank inflow rate less than the big pipe flow rate
            tank_inflow_rate = round(big_pipe_flow_rate * random.uniform(0.5, 0.9), 3)
        else:
            # No leak, tank inflow rate equals the big pipe flow rate
            tank_inflow_rate = big_pipe_flow_rate
        
        data.append([big_pipe_flow_rate, tank_inflow_rate, time_period, tank_volume])
    
    return data

# Function to save the data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['big_pipe_flow_rate', 'tank_inflow_rate', 'time_period', 'tank_volume'])
        writer.writerows(data)

# Generate and save the data
num_records = 100  
leak_ratio = 0.1  # 10% of the records will simulate leaks
synthetic_data = generate_synthetic_data_with_leaks(num_records, leak_ratio)
save_to_csv(synthetic_data, 'synthetic_water_data_with_leaks.csv')

print(f"Generated {num_records} records with leaks in {leak_ratio*100}% of them, and saved to synthetic_water_data_with_leaks.csv")