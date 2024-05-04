# Pie Charts


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Organize and visualize data in Pie Charts using pandas ########################

# If you wanted to have interactive, you could parameterize the groupby and aggregation labels.

######## Scenario 1: Use a Pie chart to show the distribution of flights by distance buckets  ##########
## Plan: Create distance bins, group by bins, plot ##

# Creating distance bins
distance_bins = pd.cut(df['Distance'], bins=[0, 500, 1000, 2000, 3000, 4000, df['Distance'].max()])

# Grouping by distance bins and aggregating by sum of flights
distance_groups = df.groupby(distance_bins).agg({'Flights': 'sum'})

# Plot
distance_groups.plot(kind='pie', y='Flights', title='Distribution of Flights by Distance')
plt.tight_layout()
plt.show()

######## Scenario 2: Use a Pie chart to show the distribution of passengers by routes (top 50)  ##########
## Plan: Group by origin & Dest cities, aggregate sum of passengers, select top 50, plot ##

# Grouping by origin and destination cities and aggregating by sum of passengers
route_groups = df.groupby(['Origin City', 'Destination City']).agg({'Passengers': 'sum'})

# Selecting the top 50 routes by passenger numbers
top_50_routes = route_groups.nlargest(50, 'Passengers')

# Plot
top_50_routes.plot(kind='pie', y='Passengers', title='Distribution of Passengers by Route')
plt.tight_layout()
plt.show()