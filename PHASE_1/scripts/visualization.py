import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv('../../data/Spotify_Youtube.csv')

def distribution(column_name: str):
    if column_name in data.columns and pd.api.types.is_numeric_dtype(data[column_name]):
        plt.figure(figsize=(10, 6))
        plt.hist(data[column_name].dropna(), bins=30, edgecolor='black')
        plt.title(f'Distribution of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    else:
        print(f"The '{column_name}' column is either missing or not numeric in the dataset.")

def comparison(column_1_name: str, column_2_name: str):
    if column_1_name in data.columns and column_2_name in data.columns:
        if pd.api.types.is_numeric_dtype(data[column_1_name]) and pd.api.types.is_numeric_dtype(data[column_2_name]):
            filtered_data = data[[column_1_name, column_2_name]].dropna().reset_index(drop=True)

            Q1 = filtered_data.quantile(0.25)
            Q3 = filtered_data.quantile(0.75)
            IQR = Q3 - Q1

            filtered_data = filtered_data[
                ~((filtered_data < (Q1 - 1.5 * IQR)) | (filtered_data > (Q3 + 1.5 * IQR))).any(axis=1)
            ]

            x = filtered_data[column_1_name]
            y = filtered_data[column_2_name]

            slope, intercept, r_value, p_value, std_err = linregress(x, y)
            regression_line = slope * x + intercept

            x_stddev = x.std()
            x_var = x.var()
            y_stddev = y.std()
            y_var = y.var()

            plt.figure(figsize=(10, 6))
            plt.scatter(x, y, alpha=0.5, label='Data Points')
            plt.plot(x, regression_line, color='red', label=f'Regression Line (R² = {r_value**2:.2f})')
            plt.title(f'Relationship between {column_1_name} and {column_2_name} (Outliers Removed)')
            plt.xlabel(column_1_name)
            plt.ylabel(column_2_name)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()

            print(f"Regression details for {column_1_name} vs {column_2_name} (Outliers Removed):")
            print(f"  Slope:            {slope:.3e}")
            print(f"  Intercept:        {intercept:.3e}")
            print(f"  R-squared:        {r_value**2:.3e}")
            print(f"  P-value:          {p_value:.3e}")
            print(f"  Standard error:   {std_err:.3e}")
            print()
            print(f"Standard deviation and variance for {column_1_name} (Outliers Removed):")
            print(f"  Standard Deviation:   {x_stddev:.3e}")
            print(f"  Variance:             {x_var:.3e}")
            print()
            print(f"Standard deviation and variance for {column_2_name} (Outliers Removed):")
            print(f"  Standard Deviation:   {y_stddev:.3e}")
            print(f"  Variance:             {y_var:.3e}")
        else:
            print(f"The '{column_1_name}' or '{column_2_name}' columns are not numeric in the dataset.")
    else:
        print(f"The '{column_1_name}' or '{column_2_name}' columns are missing in the dataset.")

# distribution('Likes')
comparison('Stream', 'Views')