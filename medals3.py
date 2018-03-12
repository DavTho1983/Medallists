import pandas as pd

medallists = pd.read_csv('Summer_Olympic_medallists_1896_to_2008.tsv', sep='\t', header=4)

"""Using .nunique() to rank by distinct sports"""

# Group medals by 'NOC': country_grouped
country_grouped = medallists.groupby('NOC')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))
