import pandas as pd
import numpy as np
import shutil
from tabulate import tabulate


def print_space():
    print('\n')

def print_break():
    print('\n' + '---' * 40 + '\n')
    
def print_part_break():
    print('\n' + '===' * 40)
    print('===' * 40 + '\n')

"""
Part 1: Summary statistics
- load the dataset
- Basic dataset info
    - Shape and size
    - Head and Tail check
    - Column Names and Data types
    - Memory usage
- Descriptive statistics
    - Mean, median, mode
    - Standard deviation
    - Min/max values
    - Quartiles
    - Unique values for categorical
    - Top Value frequency
- Percentage of missing values
"""

print("Exploratory Data Analysis of Spotify and Youtube Dataset")
print("Part 1: Summary Statistics")
print_space()

# Load Dataset
raw_dataset = pd.read_csv('data/Spotify_Youtube.csv')

# Shape and size
print(f"Dataset shape has {raw_dataset.shape[0]} rows and {raw_dataset.shape[1]} columns")
print_space()

# Set display options
pd.set_option('display.max_columns', None)

# View first few rows
print('First Few Rows:')
print(raw_dataset.head())
print_space()

print('Last Few Rows:')
print(raw_dataset.tail())
print_space()

# Get column names and data types
print('Column Names and Data Types:')
print(raw_dataset.info())
print_space()

# Memory usage
print(f"Memory usage: {raw_dataset.memory_usage().sum()} bytes")
print_space()

print_break()

# Descriptive statistics

# Get terminal width
terminal_width = shutil.get_terminal_size().columns

# Summary Statistics
print('Summary Statistics for Numerical Columns:')
summary_numerical = raw_dataset.describe(include=[np.number]).T
summary_numerical.to_csv('summary_numerical.csv')

# Format using tabulate
print(tabulate(summary_numerical, headers='keys', tablefmt='psql', floatfmt='.9f', showindex=True))
print_space()

print('Standard Deviations which are noteably too large or too small compared to their range or IQR:')
for row in summary_numerical.iterrows():
    range = row[1]['max'] - row[1]['min']
    iqr_range = row[1]['75%'] - row[1]['25%']
    std_percentage_of_range = row[1]['std'] / range * 100
    std_percentage_of_iqr_range = row[1]['std'] / iqr_range * 100
    
    if std_percentage_of_range < 15 or std_percentage_of_range > 30:
        print(f'Range - {row[0]}: {std_percentage_of_range:.3f}%')
    if std_percentage_of_iqr_range < 50 or std_percentage_of_iqr_range > 100:
        print(f'IQR - {row[0]}: {std_percentage_of_iqr_range:.3f}%')
print_space()

# Same for categorical
print('Summary Statistics for Categorical Columns:')
summary_categorical = raw_dataset.describe(include=['object']).T
summary_categorical.to_csv('summary_categorical.csv')
print(tabulate(summary_categorical, headers='keys', tablefmt='psql', showindex=True))
print_space()

print_break()

# Percentage of missing values
print('Percentage of Missing Values:')
for column in raw_dataset.columns:
    missing_values = raw_dataset[column].isnull().sum()
    percentage_missing = missing_values / raw_dataset.shape[0] * 100
    print(f'{column}: {percentage_missing:.2f}% missing values')
print_space()

print_break()

#############################################
# Assessment
#############################################

print("This assessment is brief and done in about an hour, so it is definitely not complete. I proper assessment should take a few days to a week")

print("Assessment of Part 1: Summary Statistics")
print("The dataset has 20,000+ records in it with 28 columns, this is a good size for analysis, but may have too many features")
print("From looking at the first few rows, the dataset has a mix of numerical and categorcal variables. A few of the features may be useless like 'description', 'Url_youtube', 'Uri', 'Url_spotify', which are essentially IDs")
print("There are 12 categorical variables and 16 numerical variables in the dataset")
print("The dataset has a memory usage of 4.5MB, which is not too large")
print("Looking at the numerical summary statistics, you can see that there are a number of features with too small or too large standard deviations compared to their range or IQR, indicating potential outliers and distributions that are not normal. Noteably, 'Instrumentalness' and 'Comments'")
print("Looking at the categorical summary statistics, there are a number of features with a large number of unique values, indicating that they may be high cardinality features. Description also has a large number of missing values. Looks like there is only 2079 artists, so artists have multiple songs. There are more album related songs than single songs. Most frequent track appears 24 times, might be duplicates. ")
print("Looks like spotify-related features have 0-0.1% missing values, and youtube has 2.27-4.23% missing values, so there is a data quality difference. 'Description' has the most missing values. Rates are still low (<5%) so wont be too bias")

print_part_break()

"""
Part 2: Data visualisation
- Univariate analysis
    - Histograms for numeric variables
    - Box plots for outlier detection
    - Bar plots for categorical variables
    - KDE plots for distributions
- Bivariate analysis
    - Scatter plots between numeric variables
    - Bar plots grouped by categories
    - Line plots for trends
    - Box plots across categories
- Multivariate analysis
    - Heatmaps for correlation
"""

"""
Part 3: Correlation Analysis
- Numeric correlations
    - Pearson correlation
    - Spearman correlation
    - Correlation matrix heatmap
- Categorical associations
    - Chi-square test
- Feature Importance
    - ANOVA test
"""

"""
Part 4: Data Cleaning and Preprocessing
- Handling missing values
    - Identify patterns in missing data
    - Imputation strategies
    - Remove or fill missing values
- Handle outliers
    - IQR Method or Z-score method
    - Domain specific rules
- Fix inconsistencies
    - Standardise text data
    - Remove duplicates
"""

"""
Part 5: Feature Engineering (not dimension reduction)
- Create new features
    - Mathematical transformations
    - Date-time features
    - Interaction terms
- Handle categorical variables
    - Encoding (one-hot, label, target)
    - Feature crossing
- Transform numerical variables
    - Scaling/normalisation
    - Log transofmrations
    - Polynomial features
"""
