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

## 5. Analysis and Results (Your Part)

*(**Instructions:** Fill this section with the key insights you discovered from your analysis in both Python and Power BI.)*

### Key Findings:
- **Fare Patterns:**
    - *Describe the typical fare amount. What are the most common fare ranges?*
    - *How does the time of day (peak vs. off-peak) affect fare prices?*
- **Ride Patterns:**
    - *What are the busiest hours, days of the week, and months for Uber rides?*
    - *Are there noticeable differences in ride volume between weekdays and weekends?*
- **Correlations:**
    - *What is the relationship between distance and fare amount? Is it linear?*
    - *Are there any surprising seasonal trends?*

---

## 6. Power BI Dashboard

*(**Instructions:** Add screenshots of your Power BI dashboard here. You can drag and drop images directly into this README file on GitHub.)*

**Screenshot 1: Main Dashboard Overview**
![Main Dashboard]()

**Screenshot 2: Fare Analysis View**
![Fare Analysis]()

---

## 7. Conclusion and Recommendations

*(**Instructions:** Summarize your main findings and provide actionable recommendations based on your data.)*

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