# colony_generator.py

import pandas as pd
import random
import os

# Function to determine pipe size based on the number of houses
def determine_pipe_size(num_houses):
    if 1 <= num_houses <= 5:
        return '5 inches'
    elif 6 <= num_houses <= 10:
        return '10 inches'
    elif 11 <= num_houses <= 15:
        return '15 inches'
    else:
        return 'Unknown'

# Function to generate data for a single colony
def generate_colony_data(num_rows):
    data = {
        "Row": [f"Row {i+1}" for i in range(num_rows)],
        "Number of Houses": [random.randint(5, 15) for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    df['Pipe Size'] = df['Number of Houses'].apply(determine_pipe_size)
    return df

# Function to generate CSV files for multiple colonies in a ward
def generate_colony_csv_files(ward_number, num_colonies, output_dir='wards'):
    ward_dir = os.path.join(output_dir, f'ward_{ward_number}')
    if not os.path.exists(ward_dir):
        os.makedirs(ward_dir)
    
    for colony_number in range(1, num_colonies + 1):
        num_rows = random.randint(100, 200)
        df = generate_colony_data(num_rows)
        file_path = os.path.join(ward_dir, f'colony_{colony_number}.csv')
        df.to_csv(file_path, index=False)
        print(f"Generated {file_path}")
