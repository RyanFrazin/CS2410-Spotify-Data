#using this script to narrow down popularity metrics to only focus on popularity levels 70-100
import pandas as pd

# Assuming the data is in a CSV file and has a column named 'popularity'
data = pd.read_csv('dataset.csv')

# Narrow down the data to only include popularity levels 0-100
narrowed_data = data[(data['popularity'] >= 0) & (data['popularity'] <= 100)]

#I want to focus on only certain variables, so only certain columns will be added to the narrowed data
columns_to_keep = ['popularity', 'track_name', 'track_id', 'danceability', 'energy', 'loudness', 'valence', 'speechiness', 'acousticness', 'instrumentalness', 'liveness','explicit']
narrowed_data = narrowed_data[columns_to_keep]

#drop duplicates
narrowed_data = narrowed_data.drop_duplicates()

# Save the narrowed data to a new CSV file
narrowed_data.to_csv('narrowed_popularity_data.csv', index=False)
print("Narrowed data saved to 'narrowed_popularity_data.csv'")

#display the narrowed data
print(narrowed_data.describe())
