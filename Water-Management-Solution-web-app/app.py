from flask import Flask, render_template
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
app = Flask(__name__)

# Function to calculate volume based on pipe size
def calculate_volume(num_houses, pipe_size):
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
                    df['Pipe Size'] = '15 inches'
                for _, row in df.iterrows():
                    num_houses = row['Number of Houses']
                    pipe_size = row['Pipe Size']
                    total_volume += calculate_volume(num_houses, pipe_size)
    return total_volume

# Model 1 function
def run_model1():
    base_variable_dir = 'data//wards//ward_'
    base_constant_dir = 'data//old_wards//ward_'

    variable_volumes = []
    constant_volumes = []

    for i in range(1, 85):
        ward_number = f'{i}'
        variable_pipe_size_dir = base_variable_dir + ward_number
        constant_pipe_size_dir = base_constant_dir + ward_number

        variable_total_volume = calculate_total_volume(variable_pipe_size_dir)
        constant_total_volume = calculate_total_volume(constant_pipe_size_dir, constant_pipe_size=True)

        variable_volumes.append(variable_total_volume)
        constant_volumes.append(constant_total_volume)

    ward_numbers = [f'Ward {i}' for i in range(1, 85)]

    plt.figure(figsize=(12, 8))
    width = 0.35
    x = range(len(ward_numbers))

    plt.bar([p - width/2 for p in x], variable_volumes, width=width, label='Variable Pipe Size Wards', color='blue')
    plt.bar([p + width/2 for p in x], constant_volumes, width=width, label='Constant Pipe Size Wards', color='red')

    plt.xlabel('Ward')
    plt.ylabel('Total Volume')
    plt.title('Total Volume Comparison: Variable vs Constant Pipe Size Wards')
    plt.xticks(x, ward_numbers, rotation=90)
    plt.legend()
    plt.tight_layout()

    graph_path = 'graphs/model1_output.png'
    plt.savefig(os.path.join('static', graph_path))
    plt.close()
    return graph_path

# Model 2 function
def run_model2():
    variable_pipe_size_dir = 'data//wards//ward_1'
    constant_pipe_size_dir = 'data//old_wards//ward_1'

    variable_total_volume = calculate_total_volume(variable_pipe_size_dir)
    constant_total_volume = calculate_total_volume(constant_pipe_size_dir, constant_pipe_size=True)

    labels = ['Variable Pipe Size Wards (New Layout)', 'Constant Pipe Size Wards (Old Layout)']
    volumes = [variable_total_volume, constant_total_volume]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, volumes, color=['blue', 'green'])
    plt.xlabel('Ward Type')
    plt.ylabel('Total Volume')
    plt.title('Total Volume Comparison: Variable vs Constant Pipe Size Wards')

    graph_path = 'graphs/model2_output.png'
    plt.savefig(os.path.join('static', graph_path))
    plt.close()
    return graph_path

def determine_pipe_size(num_houses):
    if 1 <= num_houses <= 5:
        return '5 inches'
    elif 6 <= num_houses <= 10:
        return '10 inches'
    elif 11 <= num_houses <= 15:
        return '15 inches'
    else:
        return 'Unknown'

def update_csv_with_pipe_size(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)
    df['Pipe Size'] = df['Number of Houses'].apply(determine_pipe_size)
    df.to_csv(output_csv_path, index=False)
    return df

def visualize_and_save_pipe_sizes(dataframe, output_image_path):
    pipe_size_counts = dataframe['Pipe Size'].value_counts()

    plt.figure(figsize=(10, 6))
    pipe_size_counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red'])
    plt.title('Distribution of Pipe Sizes in Colonies')
    plt.xlabel('Pipe Size')
    plt.ylabel('Number of rows')
    plt.xticks(rotation=0)

    plt.savefig(output_image_path)
    plt.close()

def run_model4():
    input_csv_path = 'data//csv//colony_houses.csv'
    output_csv_path = 'data//csv//colony_houses_with_pipe_size.csv'
    output_image_path = 'static//graphs//pipe_size_distribution.png'

    df = update_csv_with_pipe_size(input_csv_path, output_csv_path)
    visualize_and_save_pipe_sizes(df, output_image_path)
    return 'graphs/pipe_size_distribution.png'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_model/<model_name>')
def run_model(model_name):
    if model_name == 'model1':
        output = run_model1()
    elif model_name == 'model2':
        output = run_model2()
    elif model_name == 'model4':
        output = run_model4()
        
    else:
        output = None
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
