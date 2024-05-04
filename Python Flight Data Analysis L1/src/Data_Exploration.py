# Data Exploration

# Project Goals:
    # To load, analyze, and visualize the dataset of nearly 3.5 million rows of flight data made available by the United States using Python, NumPy, and pandas.
    # We will be loading and saving data in CSV formats, filtering, grouping, and aggregating data with pandas, and visualizing the data with pandas and Matplotlib, including bar, line, pie, and more charts.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')
print(df.head(10))

####################### Data Exploration ########################

#### Examining the DataFrame ####

# Prints a list of all columns and their datatypes.
print(df.info())

## Categorical and Numerical Data ##
# Data is generally in one of two categories: numeric and categorical. Numeric data is represented by a number and can have mathematical operations.
# Categorical (Non-numerical) data would be like an airport code, even if it is just a number, it doesn't make sense to add or divide.

## Checking for Null Values ##
# By summing the isnull() function on the DataFrame, we return the number of null values in the dataframe. None in this dataset, or we would have to use data cleaning techniques.
print(df.isnull().sum())

## Descriptive Statistics ##
# By rounding df.describe() to '2', we return a non-scientific notation format. Drops categorical data columns automatically.
print(df.describe().round(2))

## Understanding Categorical Data ##
print(df['Origin'].value_counts()) # Count of unique values
print(df['Origin'].unique())  # Unique values
print(df['Origin'].nunique()) # Number of unique values