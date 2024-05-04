# Filtering

# Definition of Filtering: Narrowing down a dataset to a subset of rows that meet certain criteria or conditions, ee.g. flights from a specific year, or exceptionally busy routes.
# Pandas provides boolean indexing to select only rows that meet a certain condition, using the 'isin()' method, and others such as the query method for SQL-like querying syntax.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Filtering ########################

######## Scenario 1: Extract records for flights only in the year 2000 ##########
## Plan: Extract the 'year' part from the 'Fly Date' column and create a new column 'Year' to hold this data. Then filter data to include only records where 'Year' is 2000 ##
df['Year'] = df['Fly Date'].astype(str).str.slice(0,4).astype(int)
flights_in_2000 = df[df['Year'] == 2000]

######## Scenario 2: Find flights that do NOT include 'LAX' as an origin ##########
## Plan: Use 'isin()' function with '~' negation operator. This returns all flights EXCEPT those originating from LAX. ##
non_lax_flights = df[~df['Fly Date'].isin(['LAX'])]

#Returns flights ONLY from 'LAX'
only_lax_flights = df[df['Origin'].isin(['LAX'])]

####################### Filtering with Multiple Conditions ########################

######## Scenario 1: Filter for flights with over 100 passengers that cover a distance of less than 1000 miles. ########
## Plan: Use the logical AND operator (&) to combine our conditions. Create two separate subqueries for passenger and distance conditions, then link with & operator ##
passengers_and_distance = df[(df['Fly Date'] > 100) & (df['Distance'] < 1000)]

######## Scenario 2: Filter for flights that are either to or from NY or LA ########
## Plan: Use the logical OR operator (|) in conjunction with the string method str.contains() to check if either city is contained in the 'Origin City' or 'Destination City' columns ##
popular_city_flights = df[df['Origin City'].str.contains('New York|Los Angeles') | 
                           df['Destination City'].str.contains('New York|Los Angeles')]

######## Scenario 3: Finding Underbooked Routes with the Query Method #########
## Plan: Use query method to filter flights where the number of seats is greater than the number of passengers. ##
new_var = df.query('Seats > Passengers') # Query function allows us to query the columns of a dataframe with a boolean expression. This filters out all rows where the number of seats is greater than the number of passengers.

######## Scenario 4: Using Logical Operators with the Query Method #########
## Plan: Use query method and logiccal AND operator (&) to find flights that are both short haul (<500mi) and very busy (>10 flts/mo) ##
df.query('Distance < 500 & Flights > 10') # Returns all rows where distance < 500 & flights > 10

####################### Saving Filtered Data Sets as CSV Files ########################

df.to_csv('new_file.csv') # Saves the dataframe 'df' into a new CSV file named 'new_file.csv'. If no specific path is given, it will create it in the current directory.