import pandas as pd
import sys
import numpy as np

# Load the cleaned dataset
try:
    df = pd.read_csv('output/uber_cleaned.csv')
    print("Cleaned dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'output/uber_cleaned.csv' not found.", file=sys.stderr)
    print("Please run the uber_eda.py script first to generate the cleaned data.", file=sys.stderr)
    sys.exit(1)

# --- Feature Engineering ---
# Calculate distance using Haversine formula
def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

# Add distance column
if all(col in df.columns for col in ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']):
    df['distance'] = haversine(df['pickup_longitude'], df['pickup_latitude'],
                               df['dropoff_longitude'], df['dropoff_latitude'])
    print("Calculated 'distance' column using Haversine formula.")
else:
    print("Warning: Latitude/longitude columns missing. 'distance' not calculated.")

# Identify and convert timestamp column
time_col = None
time_cols_to_check = [col for col in df.columns if 'time' in col.lower() or 'date' in col.lower() or 'pickup' in col.lower()]

if not time_cols_to_check:
    print("Warning: No potential timestamp column found. Skipping time-based feature engineering.")
else:
    for col in time_cols_to_check:
        try:
            # Try converting column to datetime, coercing errors
            temp_times = pd.to_datetime(df[col], errors='coerce')
            # Check if conversion was successful for a good portion of the data
            if temp_times.notnull().sum() > len(df) * 0.8:
                time_col = col
                df[time_col] = temp_times
                print(f"Successfully converted '{time_col}' to datetime.")
                break
        except Exception:
            continue

    if time_col:
        # 1. Extract time-based features
        df['hour'] = df[time_col].dt.hour
        df['day'] = df[time_col].dt.day
        df['month'] = df[time_col].dt.month
        df['day_of_week'] = df[time_col].dt.day_name()
        print("Extracted: hour, day, month, day_of_week")

        # Add season column based on month
        def month_to_season(month):
            if month in [12, 1, 2]:
                return 'Winter'
            elif month in [3, 4, 5]:
                return 'Spring'
            elif month in [6, 7, 8]:
                return 'Summer'
            elif month in [9, 10, 11]:
                return 'Autumn'
            else:
                return 'Unknown'
        df['season'] = df['month'].apply(month_to_season)
        print("Created 'season' feature.")

        # 2. Create peak/off-peak indicator (1 for peak, 0 for off-peak)
        # Peak hours: 7-9 AM (morning) and 4-7 PM (evening)
        df['is_peak_hour'] = df['hour'].apply(lambda x: 1 if (7 <= x <= 9) or (16 <= x <= 19) else 0)
        print("Created 'is_peak_hour' feature.")

        # 3. Create weekend indicator (1 for weekend, 0 for weekday)
        df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x in ['Saturday', 'Sunday'] else 0)
        print("Created 'is_weekend' feature.")

# Save the enhanced dataset
enhanced_output_path = 'output/uber_enhanced_for_powerbi.csv'
df.to_csv(enhanced_output_path, index=False)

print(f'\n--- Enhanced Data Saved ---')
print(f'Saved enhanced dataset to {enhanced_output_path}') 