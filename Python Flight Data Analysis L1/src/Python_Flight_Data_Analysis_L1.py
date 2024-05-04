# Flight Data Analysis
# Dataset has over 3.6 Million Rows

# Summary:
    # Loading and Saving Data using CSV
    # Filtering, Grouping, and Aggregating Data
    # Data Visualization
    # Intermediate Pandas Functionality such as 'cut' function & other utilities for managing & altering data.

# Scatter Plots and Histograms


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Scatter Plots ########################

# If you wanted to have interactive, you could parameterize the groupby and aggregation labels.

######## Scenario 1: Routes by distance and # of passengers  ##########
## Plan: Group by origin & destination, aggregate by distance & passengers, plot ##

route_groups = df.groupby(['Origin', 'Destination']).agg({'Distance': 'mean', 'Passengers': 'sum'})

route_groups.plot(kind='scatter', x='Distance', y='Passengers')
plt.title('Number of Passengers by Distance')
plt.xlabel('Distance')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()

####################### Histograms ########################

######## Scenario 1: Routes by distance and # of passengers  ##########
## Plan: take distance column from dataframe and plot directly ##

df['Distance'].plot(kind='hist')
plt.title('Distribution of Distances')
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

####################### EXERCISE: Correlating City Populations with Flights and Passengers ########################
## Plan: Find total city poplation of route and total number of passengers for that route in a given year. Group by year to view change over time. Then plot in scatterplot. ##

df['Total City Population'] = df['Origin Population'] + df['Destination Population']
df['Year'] = df['Fly Date'].astype(str).str.slice(0, 4)
city_populations = df.groupby(['Origin', 'Destination', 'Year']).agg({'Passengers': 'sum', 'Total City Population': 'sum'}).reset_index().sort_values(by='Year')

city_populations.plot(kind='scatter', x='Total City Population', y='Passengers')
plt.title('Number of Passengers by Total City Population')
plt.xlabel('Total City Population')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()