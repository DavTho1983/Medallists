import pandas as pd

medallists = pd.read_csv('Summer_Olympic_medallists_1896_to_2008.tsv', sep='\t', header=4)
by_medal = medallists.groupby(['Medal', 'NOC'])
count_by_medal = by_medal['Medal'].count()
print(count_by_medal.tail())

medallists_1996 = medallists.loc[medallists['Edition'] == 1996]
print(medallists_1996.head())
print(medallists_1996['Discipline'].unique())

beach_volley_medals_1996 = medallists_1996.loc[medallists['Discipline'] == 'Beach volley.']

# Select the 'NOC' column of medals: country_names
country_names_beach_volley_medals_1996 = beach_volley_medals_1996.loc[:, 'NOC']

# Count the number of medals won by each country: medal_counts
medal_counts_beach_volley_1996 = country_names_beach_volley_medals_1996.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts_beach_volley_1996.head())

# Construct the pivot table: counted
counted_1996 = medallists_1996.pivot_table(index='NOC', values='Athlete', columns=['Medal', 'Edition'], aggfunc='count')

# Create the new column: counted['totals']
counted_1996['totals'] = counted_1996.sum(axis='columns')

# Sort counted by the 'totals' column
counted_1996 = counted_1996.sort_values(by='totals', ascending=False)

# Print the top 15 rows of counted
print(counted_1996.head(15))
