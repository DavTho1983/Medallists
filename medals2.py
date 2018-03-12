import pandas as pd

medallists = pd.read_csv('Summer_Olympic_medallists_1896_to_2008.tsv', sep='\t', header=4)
# Group medals by the two columns: medals_by_gender
medallists_by_gender = medallists.groupby(['Event_gender', 'Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medallists_count_by_gender = medallists_by_gender.count()

# Print medal_count_by_gender
print(medallists_count_by_gender)

data_error = medallists[(medallists['Event_gender'] == 'W') & (medallists['Gender'] == 'Men')]
print(data_error)
