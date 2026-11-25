#This script will find the correlation for each column with popularity
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

narrowed_data = pd.read_csv('narrowed_popularity_data.csv')

correlations = narrowed_data.select_dtypes(include=['number']).corr()['popularity'].drop('popularity')
print(correlations)

# Visualize the correlations using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(narrowed_data.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for Narrowed Data')
plt.show()