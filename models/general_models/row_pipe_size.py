# import pandas as pd

# # Function to determine pipe size based on the number of houses
# def determine_pipe_size(num_houses):
#     if 1 <= num_houses <= 5:
#         return '5 inches'
#     elif 6 <= num_houses <= 10:
#         return '10 inches'
#     elif 11 <= num_houses <= 15:
#         return '15 inches'
#     else:
#         return 'Unknown'

# # Function to update the CSV file with pipe size information
# def update_csv_with_pipe_size(input_csv_path, output_csv_path):
#     # Read the CSV file
#     df = pd.read_csv(input_csv_path)
    
#     # Determine pipe size for each row
#     df['Pipe Size'] = df['Number of Houses'].apply(determine_pipe_size)
    
#     # Save the updated DataFrame to a new CSV file
#     df.to_csv(output_csv_path, index=False)

# # Paths for the input and output CSV files
# input_csv_path = 'images_result//colony_houses.csv'
# output_csv_path = 'dataofgrpahs//colony_houses_with_pipe_size.csv'

# # Update the CSV file
# update_csv_with_pipe_size(input_csv_path, output_csv_path)

import pandas as pd
import matplotlib.pyplot as plt

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
    
    return df

# Paths for the input and output CSV files
input_csv_path = 'images_result//colony_houses.csv'
output_csv_path = 'dataofgrpahs//colony_houses_with_pipe_size.csv'

# Update the CSV file and get the updated DataFrame
df = update_csv_with_pipe_size(input_csv_path, output_csv_path)

# Function to visualize and save the data as a PNG file
def visualize_and_save_pipe_sizes(dataframe, output_image_path):
    # Count the occurrences of each pipe size
    pipe_size_counts = dataframe['Pipe Size'].value_counts()
    
    # Create a bar graph
    plt.figure(figsize=(10, 6))
    pipe_size_counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red'])
    plt.title('Distribution of Pipe Sizes in Colonies')
    plt.xlabel('Pipe Size')
    plt.ylabel('Number of rows')
    plt.xticks(rotation=0)
    
    # Save the figure as a PNG file
    plt.savefig(output_image_path)
    plt.close()

# Path to save the PNG file
output_image_path = 'dataofgrpahs//pipe_size_distribution.png'

# Visualize and save the updated data
visualize_and_save_pipe_sizes(df, output_image_path)
