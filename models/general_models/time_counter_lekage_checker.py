import pandas as pd
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

def read_data(colony_name):
    try:
        return pd.read_csv(f'dataofgrpahs//leak_colony//data_{colony_name}.csv')
    except FileNotFoundError:
        print(f"File data_{colony_name}.csv not found.")
        return pd.DataFrame(columns=['timestamp', 'tank_level'])

def check_anomaly(colony_name, data, anomaly_colony):
    expected_fill_time = timedelta(minutes=colonies[colony_name]['expected_fill_time'])
    
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.sort_values('timestamp')
    
    fill_start_time = None
    fill_start_level = None
    
    for i in range(1, len(data)):
        current_time = data.iloc[i]['timestamp']
        current_level = data.iloc[i]['tank_level']
        prev_time = data.iloc[i-1]['timestamp']
        prev_level = data.iloc[i-1]['tank_level']
        
        level_diff = current_level - prev_level
        
        if fill_start_time is None and level_diff > 0:
            fill_start_time = prev_time
            fill_start_level = prev_level
        
        if fill_start_time is not None and (current_level >= 100 or level_diff == 0):
            fill_duration = current_time - fill_start_time
            if colony_name == anomaly_colony and fill_duration < expected_fill_time - timedelta(minutes=3):
                return {
                    'colony': colony_name,
                    'timestamp': current_time,
                    'duration': fill_duration.total_seconds() / 60,
                    'expected': expected_fill_time.total_seconds() / 60
                }
            fill_start_time = None
            fill_start_level = None
    
    return None

def main():
    anomaly_colony = random.choice(list(colonies.keys()))
    anomaly_detected = False

    for colony_name in colonies.keys():
        data = read_data(colony_name)
        if not data.empty:
            anomaly = check_anomaly(colony_name, data, anomaly_colony)
            print(f"\nColony {colony_name}:")
            if anomaly:
                print(f"Anomaly detected:")
                print(f"Timestamp: {anomaly['timestamp']}")
                print(f"Actual empty time: {anomaly['duration']:.2f} minutes")
                print(f"Expected empty time: {anomaly['expected']} minutes")
                anomaly_detected = True
            else:
                print("No anomalies detected.")
        else:
            print(f"No data available for colony {colony_name}.")

    if anomaly_detected:
        print(f"\nSensor activated in colony {anomaly_colony} pipeline.")
    else:
        print("\nNo sensors activated. All colony pipelines are functioning normally.")

if __name__ == "__main__":
    main()
