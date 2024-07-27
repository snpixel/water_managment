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

# Function to generate n CSV files for n colonies
def generate_colony_csv_files(n, output_dir='colonies'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for colony_number in range(1, n + 1):
        num_rows = random.randint(100, 200)
        df = generate_colony_data(num_rows)
        file_path = os.path.join(output_dir, f'colony_{colony_number}.csv')
        df.to_csv(file_path, index=False)
        print(f"Generated {file_path}")

# Generate CSV files for n colonies
n = 10  # You can set the desired number of colonies here
generate_colony_csv_files(n)