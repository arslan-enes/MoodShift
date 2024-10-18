import pandas as pd

df = pd.read_csv('data_with_clusters.csv')

# Count the number of songs in each cluster
cluster_sizes = df['mood'].value_counts()
print(cluster_sizes)

# Group by the 'mood' (cluster) and calculate the mean of each feature
cluster_means = df.groupby('mood').mean()
print("Mean values for each feature per cluster:")
print(cluster_means)
