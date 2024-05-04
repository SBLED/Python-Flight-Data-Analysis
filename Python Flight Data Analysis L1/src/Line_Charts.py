# Line Charts


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Organize and visualize data in Line Charts using pandas ########################

# If you wanted to have interactive, you could parameterize the groupby and aggregation labels.

######## Scenario 1: Use a line chart to show how the number of flights per year has changed  ##########
## Plan: Parse flight data, group by year, find the sum of flights per year ##

# Parse our fly date as a string and slice it to grab our year, then parse it as an integer:
df['Year'] = df['Fly Date'].astype(str).str.slice(0, 4).astype(int) # To remove floating point, remove '.astype(int) to parse as string

# Group by year and find the sum of flights for each year
year_groups = df.groupby('Year').agg({'Flights': 'sum'})

# Plot
year_groups.plot(kind='line')
plt.title('Total Number of Flights per Year')
plt.xlabel('Year')
plt.ylabel('Flights')
plt.xticks(rotation=45)
plt.show()

######## Scenario 2: Plotting multiple lines on the same plot  ##########
## Plan: Plot the total number of lines and the total number of passengers per year ##

year_groups_mult = df.groupby('Year').agg({'Flights':'sum', 'Passengers':'sum'})
year_groups_mult.plot(kind='line')
plt.title('Total Number of Flights and Passengers per Year')
plt.xlabel('Year')
plt.ylabel('Number of Flights/Passengers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()