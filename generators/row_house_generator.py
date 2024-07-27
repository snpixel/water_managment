import pandas as pd
import random

# Function to generate the CSV file
def generate_colony_houses_csv(file_path, num_rows=100):
    # Generate data
    data = {
        "Row": [f"Row {i+1}" for i in range(num_rows)],
        "Number of Houses": [random.randint(4, 15) for _ in range(num_rows)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(file_path, index=False)

# File path for the CSV file
csv_file_path = 'colony_houses.csv'

# Generate the CSV file
generate_colony_houses_csv(csv_file_path)