import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import joblib

# Load your dataset (replace 'your_dataset.csv' with your actual file)
df = pd.read_csv('data.csv')

# Feature Selection - Selecting relevant features
X = df[['danceability', 'energy', 'tempo', 'valence', 'acousticness', 'liveness', 'speechiness', 'instrumentalness', 'duration_ms']]

# Build the machine learning pipeline for clustering, including missing value imputation
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),  # Step 1: Handle missing values by replacing them with the mean
    ('scaler', StandardScaler()),  # Step 2: Standardize the features
    ('pca', PCA(n_components=2)),  # Step 3: Optional PCA for dimensionality reduction (to 2D)
    ('kmeans', KMeans(n_clusters=4, random_state=42))  # Step 4: Clustering with KMeans (4 clusters as an example)
])
# Fit the pipeline on the data to form clusters
pipeline.fit(X)

# Assign the cluster labels to the dataset as 'mood'
df['mood'] = pipeline['kmeans'].labels_

df.to_csv('data_with_clusters.csv', index=False)

# Export the trained model to a file using joblib
joblib.dump(pipeline, 'spotify_mood_clustering.pkl')