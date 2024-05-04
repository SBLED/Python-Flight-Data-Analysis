# Grouping and Aggregating Results


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Grouping by Origin and Destination ########################

# When grouping by multiple variables, we can think of it as creating unique pairs of these variables, or unique combinations if there is more than two with which to group by.
# In this case, we are creating unique combinations of origin and destination that will become routes.

######## Scenario 1: Group by Origin and Destination to Identify Busiest Routes ##########
## Plan: Create Unique Combinations of Origin and Destination to create routes ##

# grouped = df.groupby(['Origin', 'Destination'])
# aggregated = grouped.agg({'Passengers': 'sum'})
# sorted_values = aggregated.sort_values(by='Passengers', ascending=False)
# print(sorted_values.head())

## Consider busiest route in terms of # of flights in addition to passengers ##

######## Scenario 2: Group by Fly Date to Identify Busiest Routes ##########
## Plan: Convert fly dates column to date/time format and create a Month column to group by ##

df['Month'] = pd.to_datetime(df['Fly Date'], format='%Y%m').dt.to_period('M') # Convert Fly Date to datetime and create Month for grouping

# Group by Month and aggregate the sum of the Flights column
grouped = df.groupby('Month')
aggregated = grouped.agg({'Flights': 'sum'})

#Sort the values of this table  by Month
sorted_values = aggregated.sort_values(by='Month')

print(sorted_values.head())
