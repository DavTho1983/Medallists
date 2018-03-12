import pandas as pd

medallists = pd.read_csv('Summer_Olympic_medallists_1896_to_2008.tsv', sep='\t', header=4)

"""Counting USA vs. USSR Cold War Olympic Medals"""

# Create the pivot table: medals_won_by_country
medals_won_by_country = medallists.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')
medals_won_by_country = medals_won_by_country.fillna(0)
print(medals_won_by_country)
# Slice medals_won_by_country: cold_war_usa_usr_medals
cold_war_usa_usr_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]
print(cold_war_usa_usr_medals)

# Correlation between USA and URS medals_by_gender
corr_USA_URS = cold_war_usa_usr_medals['URS'].corr(cold_war_usa_usr_medals['USA'], method='kendall')
print(corr_USA_URS)

# Create most_medals
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')


# Print most_medals.value_counts()
print(most_medals.value_counts())
