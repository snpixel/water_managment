import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define colonies with their respective details
colonies = {
    'A': {'houses': 10, 'expected_fill_time': 17},
    'B': {'houses': 13, 'expected_fill_time': 21},
    'C': {'houses': 8, 'expected_fill_time': 15},
    'D': {'houses': 20, 'expected_fill_time': 35},
    'E': {'houses': 40, 'expected_fill_time': 60},
    'F': {'houses': 15, 'expected_fill_time': 24},
    'G': {'houses': 12, 'expected_fill_time': 20},
    'H': {'houses': 18, 'expected_fill_time': 30},
    'I': {'houses': 25, 'expected_fill_time': 40},
    'J': {'houses': 22, 'expected_fill_time': 33}
}

def generate_data(colony_name, file_path):
    # Define parameters
    start_time = datetime.now() - timedelta(minutes=120)
    timestamps = [start_time + timedelta(minutes=i) for i in range(121)]
    tank_levels = np.linspace(0, 100, 121) + np.random.normal(0, 5, 121)

    # Introduce anomalies
    if colony_name in ['A', 'B']:
        tank_levels[-3:] = [tank_levels[-3]] * 3  # Simulate no-filling period
    if colony_name in ['C', 'D']:
        tank_levels[-5:] = [tank_levels[-5]] * 5  # Simulate no-filling period
    if colony_name in ['E', 'F']:
        tank_levels[5] = tank_levels[4] + 50  # Simulate rapid filling
    if colony_name in ['G', 'H']:
        tank_levels[10] = tank_levels[9] - 20  # Simulate a reduction in tank level
    if colony_name in ['I', 'J']:
        tank_levels[15] = tank_levels[14] + 80  # Simulate an unexpected spike in filling

    # Create DataFrame and save to CSV|
    df = pd.DataFrame({
        'timestamp': timestamps,
        'tank_level': tank_levels
    })
    df.to_csv(file_path, index=False)

# Generate data for all colonies
for colony_name in colonies.keys():
    generate_data(colony_name, f'water_managment//dataofgrpahs//leak_colony//data_{colony_name}.csv')
