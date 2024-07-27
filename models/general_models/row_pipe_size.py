import pandas as pd

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

# Function to update the CSV file with pipe size information
def update_csv_with_pipe_size(input_csv_path, output_csv_path):
    # Read the CSV file
    df = pd.read_csv(input_csv_path)
    
    # Determine pipe size for each row
    df['Pipe Size'] = df['Number of Houses'].apply(determine_pipe_size)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv_path, index=False)

# Paths for the input and output CSV files
input_csv_path = 'colony_houses.csv'
output_csv_path = 'dataofgrpahs//colony_houses_with_pipe_size.csv'

# Update the CSV file
update_csv_with_pipe_size(input_csv_path, output_csv_path)