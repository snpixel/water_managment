import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Define parameters
measurement_interval = 30  # seconds
percentage_threshold = 0.5  # percent
leakage_percentage = 0.2  # 10% of data will have leakage

# Generate sample data for volumes
def generate_pipeline_data(file_path):
    start_time = datetime.now() - timedelta(minutes=10)
    timestamps = [start_time + timedelta(seconds=i * measurement_interval) for i in range(20)]
    
    # Generate volumes
    volume_in = np.random.uniform(10, 15, 20)
    
    # Create volume_out with normal variation
    volume_out = volume_in + np.random.uniform(-0.5, 0.5, 20)  # Small random variations
    
    # Introduce random leakage
    num_leakages = int(len(volume_in) * leakage_percentage)
    leakage_indices = np.random.choice(len(volume_in), size=num_leakages, replace=False)  # Random indices for leakage
    leakage_amounts = np.random.uniform(1, 3, num_leakages)  # Random leakage amounts
    
    for idx, leakage in zip(leakage_indices, leakage_amounts):
        volume_out[idx] = volume_in[idx] - leakage  # Simulate leakage
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'volume_in': volume_in,
        'volume_out': volume_out
    })
    df.to_csv(file_path, index=False)

def check_leakage(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.sort_values('timestamp')
    
    # Calculate total volume and leakage threshold
    total_volume = data['volume_in'].sum()
    leakage_threshold = total_volume * (percentage_threshold / 100)
    
    # Calculate volume difference
    data['volume_diff'] = data['volume_in'] - data['volume_out']
    
    # Detect leakage
    anomalies = data[data['volume_diff'] > leakage_threshold]
    non_leakages = data[data['volume_diff'] <= leakage_threshold]
    
    if not anomalies.empty:
        print(f"Leakage detected with threshold: {leakage_threshold:.2f} cubic meters")
        print("Leakage Data:")
        print(anomalies)
    else:
        print("No leakage detected.")
    
    if not non_leakages.empty:
        print("\nNon-Leakage Data:")
        print(non_leakages)
    else:
        print("\nAll data points show leakage.")

def main():
    file_path = 'pipeline_data.csv'
    
    # Generate sample data
    generate_pipeline_data(file_path)
    
    # Read and analyze data
    data = pd.read_csv(file_path)
    check_leakage(data)

if __name__ == "__main__":
    main()
