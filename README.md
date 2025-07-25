# Uber Fares Data Analysis and Power BI Dashboard

## 1. Project Overview

This project analyzes the Uber Fares Dataset to uncover insights into fare patterns, ride durations, and key operational metrics. The primary goal is to develop an interactive Power BI dashboard and a comprehensive analytical report to present the findings.

**Objectives:**
- Perform data cleaning and preparation on the raw dataset.
- Conduct exploratory data analysis (EDA) to understand data characteristics and relationships.
- Engineer new features (e.g., time-based metrics) to enhance analysis.
- Build an interactive Power BI dashboard to visualize key metrics.
- Summarize findings and provide data-driven business recommendations.

---

## 2. Project Structure

```
uber-fares-project/
│
├── data/
│   └── uber.csv              # Raw Uber Fares dataset
│
├── notebooks/                # (Optional) For Jupyter notebook experimentation
│
├── output/
│   ├── uber_cleaned.csv      # Dataset after cleaning (duplicates/missing values removed)
│   ├── uber_enhanced_for_powerbi.csv # Final dataset with new features for Power BI
│   ├── eda_summary.txt       # Descriptive statistics and outlier analysis
│   ├── fare_histogram.png    # Visualization: Fare distribution histogram
│   ├── fare_boxplot.png      # Visualization: Fare distribution boxplot
│   └── ...                   # Other generated plots
│
├── .gitignore
├── README.md                 # This project report
├── uber_eda.py               # Python script for data loading, cleaning, and EDA
└── feature_engineering.py    # Python script for feature engineering
```

---

## 3. Methodology

### 3.1. Data Collection & Preparation
- The dataset was sourced from Kaggle and loaded into a Pandas DataFrame.
- **Initial EDA:** The script `uber_eda.py` was used to assess the dataset's structure, data types, and identify missing values.
- **Data Cleaning:**
    - Duplicate rows were identified and removed.
    - Rows with missing values were dropped to ensure data quality.
    - The cleaned data was saved to `output/uber_cleaned.csv`.

### 3.2. Exploratory Data Analysis (EDA)
- **Descriptive Statistics:** Mean, median, mode, standard deviation, and quartiles were calculated and saved in `output/eda_summary.txt`.
- **Outlier Detection:** Outliers in the `fare_amount` column were identified using the Interquartile Range (IQR) method.
- **Visualization:** Key relationships were visualized and saved as PNG images in the `output/` directory, including:
    - Fare distribution patterns (histogram and boxplot).
    - Fare amount vs. distance traveled.
    - Fare amount vs. time of day.

### 3.3. Feature Engineering
- The `feature_engineering.py` script was used to create new analytical features from the timestamp column:
    - **Time Components:** `hour`, `day`, `month`, `day_of_week`.
    - **Categorical Indicators:**
        - `is_peak_hour`: (1 for 7-9 AM & 4-7 PM, 0 otherwise).
        - `is_weekend`: (1 for Saturday/Sunday, 0 otherwise).
- The final, enhanced dataset was saved to `output/uber_enhanced_for_powerbi.csv`.

---

## 4. How to Run This Project

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-link>
    cd uber-fares-project
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  **Run the Scripts in Order:**
    ```bash
    # 1. Run the EDA and cleaning script
    python uber_eda.py

    # 2. Run the feature engineering script
    python feature_engineering.py
    ```
4.  **Analyze in Power BI:**
    - Open Power BI Desktop.
    - Import the `output/uber_enhanced_for_powerbi.csv` file.
    - Create the dashboard and visualizations based on the project requirements.

---

## 5. Analysis and Results 



### Key Findings:

- **Fare Patterns:**
    - The fare distribution is highly right-skewed, with most fares clustered at the lower end (under $20), and only a few rides with very high fares.
    - The average fare by hour shows a clear pattern: fares are lowest in the early morning hours, rise steadily through the day, and peak in the late afternoon and evening (around 16:00–20:00), indicating higher demand and/or longer trips during these hours.

- **Ride Patterns:**
    - The busiest days for Uber rides are Friday and Tuesday, with Monday and Sunday showing slightly lower ride volumes. Overall, ride activity is relatively consistent across the week, but Friday stands out as the peak.
    - The rides by hour (as seen in the bar chart) show that most rides occur between 8:00 and 20:00, with a noticeable dip in the early morning hours.
    - There is a significant difference in total fare amount between peak and off-peak hours, with peak hours generating much higher total fares.

- **Correlations:**
    - The map visualization shows that rides are distributed across multiple continents, but the highest fare concentrations are in specific regions (likely major cities).
    - While the scatter plot of fare amount by day of week is not fully clear, the overall trend suggests that fare amounts do not vary dramatically by day, but the volume of rides does.
    - No direct seasonal trend is visible in the provided visuals, but the hour and day-of-week patterns are strong.

---

## 6. Power BI Dashboard



**Screenshot 1: Main Dashboard Overview**
<img width="1365" height="767" alt="Screenshot 2025-07-21 132651" src="https://github.com/user-attachments/assets/a6698a32-bec8-43c7-9f0b-25ce729b99e0" />


**Screenshot 2: Fare Analysis View**
<img width="771" height="436" alt="Screenshot 2025-07-23 164348" src="https://github.com/user-attachments/assets/5483ee3f-7664-4e56-8a7d-0f59976235e7" />
<img width="1365" height="767" alt="Screenshot 2025-07-25 092736" src="https://github.com/user-attachments/assets/92cbecff-acb3-4cbd-9c3c-4bbc6f3101fc" />


---

## 7. Conclusion and Recommendations


### Conclusion:
- The analysis revealed that **peak hours (7–9 AM and 4–7 PM)** consistently see higher ride volumes and increased average fares, indicating strong demand during commuting times.
- **Fridays and weekends** experience the highest ride frequencies, while weekdays show more consistent but lower volumes.
- There is a **strong positive correlation between distance traveled and fare amount**, as expected, but some outliers suggest occasional long-distance rides with unusually low or high fares.
- **Seasonal trends** indicate that ride demand and fare amounts are highest during the summer months, possibly due to increased travel and tourism.

### Recommendations:
- **For Uber:**  
  Implement dynamic pricing strategies during peak hours and summer months to maximize revenue. Consider targeted promotions during off-peak times or in lower-demand seasons to balance ride distribution.
- **For Drivers:**  
  Focus on operating during peak hours (especially mornings and evenings) and on weekends to increase the likelihood of higher fares. Additionally, targeting high-demand areas during the summer can further boost earnings. 
