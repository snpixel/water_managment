import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = '/content/sample_ward_monthly_summary.csv'
data = pd.read_csv(file_path)

# Convert 'Month' and 'Year' into a single datetime column
data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))
data = data.sort_values('Date')

# Feature engineering
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Define features and target variables
features = ['Month', 'Year', 'Population']
target_supply = 'Water_Distributed'
target_per_capita = 'Per_Capita_Requirement'

X = data[features]
y_supply = data[target_supply]
y_per_capita = data[target_per_capita]

# Split the data into training and test sets
X_train, X_test, y_train_supply, y_test_supply, y_train_per_capita, y_test_per_capita = train_test_split(
    X, y_supply, y_per_capita, test_size=0.2, random_state=42
)

# Initialize and train the models
model_supply = RandomForestRegressor(n_estimators=100, random_state=42)
model_per_capita = RandomForestRegressor(n_estimators=100, random_state=42)

model_supply.fit(X_train, y_train_supply)
model_per_capita.fit(X_train, y_train_per_capita)

# Make predictions
y_pred_supply = model_supply.predict(X_test)
y_pred_per_capita = model_per_capita.predict(X_test)

# Evaluate the models
mae_supply = mean_absolute_error(y_test_supply, y_pred_supply)
mse_supply = mean_squared_error(y_test_supply, y_pred_supply)
mae_per_capita = mean_absolute_error(y_test_per_capita, y_pred_per_capita)
mse_per_capita = mean_squared_error(y_test_per_capita, y_pred_per_capita)

print(f'MAE for Water Distributed: {mae_supply}')
print(f'MSE for Water Distributed: {mse_supply}')
print(f'MAE for Per Capita Requirement: {mae_per_capita}')
print(f'MSE for Per Capita Requirement: {mse_per_capita}')

# Visualizations
plt.figure(figsize=(16, 12))

# Actual vs Predicted Water Distributed
plt.subplot(2, 2, 1)
sns.scatterplot(x=y_test_supply, y=y_pred_supply, alpha=0.7, color='blue')
plt.plot([y_test_supply.min(), y_test_supply.max()], [y_test_supply.min(), y_test_supply.max()], 'k--', lw=2)
plt.xlabel('Actual Water Distributed')
plt.ylabel('Predicted Water Distributed')
plt.title('Actual vs Predicted Water Distributed')

# Actual vs Predicted Per Capita Requirement
plt.subplot(2, 2, 2)
sns.scatterplot(x=y_test_per_capita, y=y_pred_per_capita, alpha=0.7, color='green')
plt.plot([y_test_per_capita.min(), y_test_per_capita.max()], [y_test_per_capita.min(), y_test_per_capita.max()], 'k--', lw=2)
plt.xlabel('Actual Per Capita Requirement')
plt.ylabel('Predicted Per Capita Requirement')
plt.title('Actual vs Predicted Per Capita Requirement')

# Distribution of Errors for Water Distributed
plt.subplot(2, 2, 3)
errors_supply = y_test_supply - y_pred_supply
sns.histplot(errors_supply, bins=20, kde=True, color='blue')
plt.xlabel('Prediction Error (Water Distributed)')
plt.ylabel('Frequency')
plt.title('Distribution of Prediction Errors (Water Distributed)')

# Distribution of Errors for Per Capita Requirement
plt.subplot(2, 2, 4)
errors_per_capita = y_test_per_capita - y_pred_per_capita
sns.histplot(errors_per_capita, bins=20, kde=True, color='green')
plt.xlabel('Prediction Error (Per Capita Requirement)')
plt.ylabel('Frequency')
plt.title('Distribution of Prediction Errors (Per Capita Requirement)')

plt.tight_layout()
plt.show()

# Make future predictions
future_dates = pd.date_range(start=data['Date'].max(), periods=12, freq='M')
future_data = pd.DataFrame({
    'Date': future_dates,
    'Month': future_dates.month,
    'Year': future_dates.year,
    'Population': data['Population'].iloc[-1]  # Assuming the population remains constant
})

X_future = future_data[features]
future_predictions_supply = model_supply.predict(X_future)
future_predictions_per_capita = model_per_capita.predict(X_future)

# Create a DataFrame with future predictions
future_predictions = pd.DataFrame({
    'Date': future_dates,
    'Predicted_Water_Distributed': future_predictions_supply,
    'Predicted_Per_Capita_Requirement': future_predictions_per_capita
})

print(future_predictions)

# Visualize future predictions
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(data['Date'], data['Water_Distributed'], label='Historical Water Distributed', color='blue')
plt.plot(future_predictions['Date'], future_predictions['Predicted_Water_Distributed'], label='Predicted Water Distributed', color='orange')
plt.xlabel('Date')
plt.ylabel('Water Distributed (liters)')
plt.title('Historical and Predicted Water Distributed')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(data['Date'], data['Per_Capita_Requirement'], label='Historical Per Capita Requirement', color='green')
plt.plot(future_predictions['Date'], future_predictions['Predicted_Per_Capita_Requirement'], label='Predicted Per Capita Requirement', color='red')
plt.xlabel('Date')
plt.ylabel('Per Capita Requirement (liters/person/day)')
plt.title('Historical and Predicted Per Capita Requirement')
plt.legend()

plt.tight_layout()
plt.show()
