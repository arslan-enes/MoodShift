import joblib
# -------------------------------------------------------------
# Usage: Loading and using the saved model for song suggestions
# -------------------------------------------------------------

# Load the model
loaded_model = joblib.load('spotify_mood_clustering.pkl')

# Function to suggest a song based on user-selected cluster (mood)
def suggest_song(user_mood, dataset):
    # Filter the dataset for songs with the user-selected mood (cluster label)
    suggested_songs = dataset[dataset['mood'] == user_mood]
    
    if not suggested_songs.empty:
        # Suggest a random song from the filtered list
        song = suggested_songs.sample(n=1)
        return {
            'artist': song['artist'].values[0],
            'name': song['name'].values[0],
            'preview_url': song['preview_url'].values[0]
        }
    else:
        return "No songs found for the selected mood."

# Example usage: Let the user choose a mood (cluster number between 0 and 3 for 4 clusters)
user_selected_mood = 2  # This would come from user input

# Suggest a song based on the selected mood (cluster)
song_suggestion = suggest_song(user_selected_mood, df)
print("Suggested Song:", song_suggestion)
