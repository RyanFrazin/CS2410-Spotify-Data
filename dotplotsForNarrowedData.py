#dotplots for narrowed data
import pandas as pd
import matplotlib.pyplot as plt

# Load the narrowed data
narrowed_data = pd.read_csv('narrowed_popularity_data.csv')

# Create dotplots for each numerical column
for column in narrowed_data.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(10, 6))
    plt.plot(narrowed_data['popularity'], narrowed_data[column], 'o')
    plt.title(f'Dotplot for {column}')
    plt.xlabel('popularity')
    plt.ylabel(column)
    plt.show()