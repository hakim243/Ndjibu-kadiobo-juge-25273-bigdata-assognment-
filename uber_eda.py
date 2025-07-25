import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv('data/uber.csv')

# Display the first few rows
print('--- Sample Rows ---')
print(df.head())

# Display the shape of the dataset
print(f'\n--- Dataset Shape ---\nRows: {df.shape[0]}, Columns: {df.shape[1]}')

# Display column names and data types
print('\n--- Columns and Data Types ---')
print(df.dtypes)

# Display summary of missing values
print('\n--- Missing Values Summary ---')
print(df.isnull().sum())

# Remove duplicate rows
num_duplicates = df.duplicated().sum()
print(f'\n--- Duplicate Rows ---\nFound {num_duplicates} duplicate rows.')
df = df.drop_duplicates()
print(f'Rows after removing duplicates: {df.shape[0]}')

# Handle missing values (drop rows with any missing values for now)
missing_before = df.isnull().sum().sum()
df = df.dropna()
missing_after = df.isnull().sum().sum()
print(f'\n--- Missing Values Handling ---')
print(f'Total missing values before: {missing_before}')
print(f'Total missing values after: {missing_after}')
print(f'Rows after dropping missing values: {df.shape[0]}')

# Save cleaned data
output_path = 'output/uber_cleaned.csv'
df.to_csv(output_path, index=False)
print(f'\n--- Cleaned Data Saved ---\nSaved cleaned dataset to {output_path}')

# --- Descriptive Statistics ---
summary = []
summary.append('--- Descriptive Statistics ---')
describe = df.describe(include='all')
summary.append(str(describe))

# Calculate mode for each column
summary.append('\n--- Mode for Each Column ---')
for col in df.select_dtypes(include=['number', 'object']).columns:
    mode_val = df[col].mode()
    summary.append(f'{col}: {mode_val.values[0] if not mode_val.empty else "No mode"}')

# Quartiles and IQR for fare and distance columns (if present)
for col in ['fare_amount', 'distance', 'Distance', 'Fare', 'fare', 'total_amount']:
    if col in df.columns:
        summary.append(f'\n--- Outlier Detection for {col} ---')
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        summary.append(f'{col} IQR: {IQR}, Lower Bound: {lower}, Upper Bound: {upper}')
        summary.append(f'Number of outliers: {outliers.shape[0]}')

# Save summary to file
with open('output/eda_summary.txt', 'w') as f:
    for line in summary:
        f.write(line + '\n')

print('\n--- EDA Summary Saved ---')
print('Descriptive statistics and outlier info saved to output/eda_summary.txt')

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

# --- Visualization: Fare Distribution ---
fare_cols = [col for col in ['fare_amount', 'Fare', 'fare', 'total_amount'] if col in df.columns]
if fare_cols:
    fare_col = fare_cols[0]
    plt.figure(figsize=(8, 5))
    sns.histplot(df[fare_col], bins=50, kde=True)
    plt.title('Fare Distribution')
    plt.xlabel('Fare Amount')
    plt.ylabel('Frequency')
    plt.savefig('output/fare_histogram.png')
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[fare_col])
    plt.title('Fare Boxplot')
    plt.xlabel('Fare Amount')
    plt.savefig('output/fare_boxplot.png')
    plt.close()

    # --- Visualization: Fare vs Distance ---
    dist_cols = [col for col in ['distance', 'Distance'] if col in df.columns]
    if dist_cols:
        dist_col = dist_cols[0]
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[dist_col], y=df[fare_col], alpha=0.3)
        plt.title('Fare Amount vs Distance')
        plt.xlabel('Distance')
        plt.ylabel('Fare Amount')
        plt.savefig('output/fare_vs_distance.png')
        plt.close()

    # --- Visualization: Fare vs Hour of Day ---
    # Try to extract hour from a timestamp column if present
    time_cols = [col for col in df.columns if 'time' in col.lower() or 'date' in col.lower() or 'pickup' in col.lower()]
    for tcol in time_cols:
        try:
            times = pd.to_datetime(df[tcol], errors='coerce')
            if times.notnull().sum() > 0:
                plt.figure(figsize=(8, 5))
                sns.scatterplot(x=times.dt.hour, y=df[fare_col], alpha=0.3)
                plt.title(f'Fare Amount vs Hour of Day ({tcol})')
                plt.xlabel('Hour of Day')
                plt.ylabel('Fare Amount')
                plt.savefig(f'output/fare_vs_hour_{tcol}.png')
                plt.close()
                break
        except Exception:
            continue

print('\n--- Visualizations Saved ---')
print('Plots saved to output/ directory.') 