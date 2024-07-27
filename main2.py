import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('combined_data.csv')

profile = ProfileReport(df)
profile.to_file(output_file="combined_data_profile.html")