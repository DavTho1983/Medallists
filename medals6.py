import pandas as pd
import matplotlib.pyplot as plt

medallists = pd.read_csv('Summer_Olympic_medallists_1896_to_2008.tsv', sep='\t', header=4)
medallists['Medal'] = pd.Categorical(values = medallists['Medal'], categories=['Bronze', 'Silver', 'Gold'], ordered=True)
"""Visualizing USA Medal Counts by Edition: Line Plot"""

# Create the DataFrame: usa
usa = medallists.loc[medallists.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()
print(usa_medals_by_year)

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')
# usa_medals_by_year = usa_medals_by_year[['Bronze', 'Silver', 'Gold']]
print(usa_medals_by_year)

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()
