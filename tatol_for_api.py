import pandas as pd
import numpy as np

# Number of wards
num_wards = 85

# Percentage of wards to spike
spike_percentage = 0.1  # 10%

# Generate sample data
np.random.seed(42)  # For reproducible results

# Create a date range for the year 2023
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')

# Function to adjust water usage based on the season
def adjust_water_usage(date, base_value):
    if date.month in [6, 7, 8]:  # Summer
        return base_value * 1.5
    elif date.month in [12, 1, 2]:  # Winter
        return base_value * 0.7
    else:  # Other months
        return base_value

# Select wards to apply spikes
spiked_wards = np.random.choice(range(1, num_wards + 1), size=int(num_wards * spike_percentage), replace=False)

# Initialize lists to store combined data
combined_data = []

# Generate data for each ward
for ward_id in range(1, num_wards + 1):
    # Generate random number of people for the ward
    num_people = np.random.randint(1000, 2000, size=len(dates))
    
    # Initialize water distributed with base value
    base_water_distributed = np.random.randint(1000, 3000, size=len(dates))
    
    # Apply the adjustment to each date and base value
    water_distributed = np.array([adjust_water_usage(date, base_value) 
                                  for date, base_value in zip(dates, base_water_distributed)])
    
    # Create DataFrame for the current ward
    df = pd.DataFrame({
        "ward_id": f"W{ward_id}",
        "date": dates,
        "num_people": num_people,
        "water_distributed_l": water_distributed
    })
    
    # Perform comparisons
    monthly_summary = df.groupby(['ward_id', df['date'].dt.to_period('M')]).agg({
        'num_people': 'sum',
        'water_distributed_l': 'sum'
    }).reset_index()
    monthly_summary['date'] = monthly_summary['date'].astype(str)  # Convert period to string
    monthly_summary['per_capita_usage_l'] = monthly_summary['water_distributed_l'] / monthly_summary['num_people']
    
    yearly_summary = df.groupby(['ward_id', df['date'].dt.to_period('Y')]).agg({
        'num_people': 'sum',
        'water_distributed_l': 'sum'
    }).reset_index()
    yearly_summary['date'] = yearly_summary['date'].astype(str)  # Convert period to string
    yearly_summary['per_capita_usage_l'] = yearly_summary['water_distributed_l'] / yearly_summary['num_people']
    
    # Introduce fluctuations and spikes in per capita usage
    monthly_summary['per_capita_usage_l'] *= np.random.uniform(0.95, 1.05, size=len(monthly_summary))
    yearly_summary['per_capita_usage_l'] *= np.random.uniform(0.95, 1.05, size=len(yearly_summary))

    # Apply a 10% spike to selected wards
    if ward_id in spiked_wards:
        monthly_summary['per_capita_usage_l'] *= 1.10
        yearly_summary['per_capita_usage_l'] *= 1.10
    
    # Calculate total based on num_people and per_capita_usage_l
    monthly_summary['total'] = monthly_summary['num_people'] * monthly_summary['per_capita_usage_l']
    yearly_summary['total'] = yearly_summary['num_people'] * yearly_summary['per_capita_usage_l']

    # Append summary type for clarity
    monthly_summary['summary_type'] = 'monthly'
    yearly_summary['summary_type'] = 'yearly'
    
    # Append to combined data list
    combined_data.append(monthly_summary)
    combined_data.append(yearly_summary)

# Combine all summaries into a single DataFrame
combined_df = pd.concat(combined_data, ignore_index=True)

# Save combined data to a single CSV file
combined_df.to_csv('combined_data.csv', index=False)

print("All data has been saved to 'combined_data.csv'.")