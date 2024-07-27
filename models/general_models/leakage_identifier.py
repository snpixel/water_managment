import csv
import matplotlib.pyplot as plt

# Function to calculate the volume of water
def calculate_volume(flow_rate, time_period):
    return flow_rate * time_period

# Function to check for leaks and collect data for plotting
def check_for_leaks(filename, threshold=3):
    volumes_pipe = []
    volumes_tank_in = []
    discrepancies = []
    potential_leaks = []
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            big_pipe_flow_rate = float(row['big_pipe_flow_rate'])
            tank_inflow_rate = float(row['tank_inflow_rate'])
            time_period = int(row['time_period'])
            tank_volume = int(row['tank_volume'])

            # Calculate volumes
            volume_pipe = calculate_volume(big_pipe_flow_rate, time_period)
            volume_tank_in = calculate_volume(tank_inflow_rate, time_period)
            
            # Compare volumes
            discrepancy = volume_pipe - volume_tank_in

            # Store data
            volumes_pipe.append(volume_pipe)
            volumes_tank_in.append(volume_tank_in)
            discrepancies.append(discrepancy)
            if abs(discrepancy) > threshold:
                potential_leaks.append(discrepancy)
            else:
                potential_leaks.append(None)  # No leak

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(volumes_pipe, label='Volume through Big Pipe', color='blue', alpha=0.6)
    plt.plot(volumes_tank_in, label='Volume into Tank', color='green', alpha=0.6)
    
    # Highlight potential leaks
    plt.scatter(range(len(potential_leaks)), potential_leaks, color='red', label='Potential Leaks', s=10, alpha=0.6)
    plt.ylim(0,600)
    
    plt.xlabel('Record Index')
    plt.ylabel('Volume (m³)')
    plt.title('Water Flow Volumes and Potential Leaks')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "_main_":
    filename = 'synthetic_water_data_with_leaks.csv'
    check_for_leaks(filename)