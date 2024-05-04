# Bar Charts


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Takes ~302mb in memory.
df = pd.read_csv('flights.csv')

####################### Organize and visualize data in Bar Charts using pandas ########################

# Using pandas' cut function allows us to categorize continuous data using an inputted column and list of desired bins.

######## Using pandas 'cut' function to organize data  ##########
## Plan: Split data into bins, with the last bin being maximum ##

# Cut columns into bins
distance_bins = pd.cut(df['Distance'], bins=[0, 500, 1000, 2000, 3000, 4000, df['Distance'].max()])

# Group data using the new bins and aggregate to explore data
grouped_data = df.groupby(distance_bins).agg({'Flights': 'sum', 'Passengers': 'sum'})

#Sort by distance
sorted_data = grouped_data.sort_values(by='Distance', ascending=False)

##  ##

######## Visualizing data with pandas  ##########
## Plan: Use matplotlib in conjunction with pandas dataframes ##

### Scenario 1: Find top 10 busiest orgin airports ###

# Group by origin and aggregate sum of flights
airport_traffic = df.groupby('Origin').agg({'Flights':'sum'})

# Select 10 airports with greatest number of flights
busiest_airports = airport_traffic.nlargest(10, 'Flights')

# Plot
busiest_airports.plot(kind='bar')
plt.title('Top 10 Busiest Airports by Outgoing Flights')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45) #Rotate x-axis label for readability purposes
plt.tight_layout() # Adjust layout to fit properly
plt.show()

### Scenario 2: Find top 10 busiest routes by passengers ###

# Group by origin and destination to get the total # of passengers for each route
route_traffic = df.groupby(['Origin', 'Destination']).agg({'Passengers': 'sum'})

# Select 10 busiest routes with greatest # of passengers
busiest_routes = route_traffic.nlargest(10, 'Passengers')

# Plot
busiest_routes.plot(kind='bar', color='darkblue')
plt.title('Top 10 Busiest Routes by Number of Passengers')
plt.ylabel('Number of Passengers')
plt.xticks(rotation=45) #Rotate x-axis labels for readability purposes
plt.tight_layout() # Adjust layout to fit properly
plt.show()

### Scenario 3: Find top 10 busiest routes by flights ###

route_flt_traffic = df.groupby(['Origin', 'Destination']).agg({'Flights': 'sum'})

busiest_flt_routes = route_flt_traffic.nlargest(10, 'Flights')

# OR, instead of the two above, can combine like this:
# busiest_flt_routes = df.groupby(['Origin City', 'Destination City']).agg({'Flights': 'sum'}).nlargest(10, 'Flights')

busiest_flt_routes.plot(kind='bar', color='darkblue')
plt.title('Top 10 Busiest Routes by Number of Flights')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()