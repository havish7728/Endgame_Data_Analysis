from characters import *

# Used to display first few rows
print(avengers_data.head())

# Get summary statistics
print(avengers_data.describe())

# Check for missing values
print(avengers_data.isnull().sum())
