"""
Part 1: Data Collection and Initial Inspection
- Load dataset
- Check dimensions (rows and columns)
- View first and last few rows
- Get column names and data types
- Check for missing values
"""

import pandas as pd
import numpy as np


def print_break():
    print('\n' + '---' * 40 + '\n')

print("Exploratory Data Analysis of Spotify and Youtube Dataset")
print("Part 1: Data Collection and Initial Inspection")

# Load Dataset
raw_dataset = pd.read_csv('data/Spotify_Youtube.csv')

# Check dimensions
print(f"Dataset has {raw_dataset.shape[0]} rows and {raw_dataset.shape[1]} columns")
print_break()


# View first few rows
print('First Few Rows:')
print(raw_dataset.head())
print_break()

print('Last Few Rows:')
print(raw_dataset.tail())
print_break()

# Get column names and data types
print('Column Names and Data Types:')
print(raw_dataset.info())
print_break()

# Check for missing values for each column
for column in raw_dataset.columns:
    print(f'{column}: {raw_dataset[column].isnull().sum()} missing values')
    

"""
Part 2: Summary Statistics
- Get summary statistics for numerical columns
- Get summary statistics for categorical columns

"""

# Summary Statistics for Numerical Columns
print('Summary Statistics for Numerical Columns:')
summary_numerical = raw_dataset.describe(include=[np.number])
summary_numerical.T.to_csv('summary_numerical.csv') # Outputs to CSV

# Summary Statistics for Categorical Columns
print('Summary Statistics for Categorical Columns:')
summary_categorical = raw_dataset.describe(include=['object'])
summary_categorical.T.to_csv('summary_categorical.csv') # Outputs to CSV
