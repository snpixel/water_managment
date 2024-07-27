# main.py
import random
import os
from colony_generator import generate_colony_csv_files

# Number of wards
num_wards = 84

# Directory to save the CSV files for all wards
output_dir = 'wards'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate data for each ward
for ward_number in range(1, num_wards + 1):
    num_colonies = random.randint(10, 20)
    generate_colony_csv_files(ward_number, num_colonies, output_dir)

print("All ward data generated.")
