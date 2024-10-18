import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="MoodShift", page_icon="🎵")

st.title(":orange[Mood]:blue[Shift] 🍃")
st.subheader("Discover the perfect soundtrack for every mood!")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])


col1, col2, col3 = tab1.columns([2,1,1], gap="small")

col2.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/19/JethroTullAqualungalbumcover.jpg/220px-JethroTullAqualungalbumcover.jpg", width=250)
col3.image("https://upload.wikimedia.org/wikipedia/tr/3/3e/Graduation-album.jpg", width=250)
col2.image("https://upload.wikimedia.org/wikipedia/en/3/35/The_Eminem_Show.jpg", width=250)
col3.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/15/HatfulofHollow84.jpg/220px-HatfulofHollow84.jpg", width=250)

col1.markdown("""

Welcome to **MoodShift**, the ultimate music experience that tunes into your emotions and shifts your vibe to match any mood. Whether you're feeling energetic, calm, intense, or reflective, **MoodShift** helps you discover the perfect soundtrack for every moment.

With **MoodShift**, we’ve analyzed key musical attributes like energy, danceability, tempo, and emotional tone to categorize songs into distinct "mood clusters." Whether you’re looking to get lost in high-energy beats or relax with mellow acoustic sounds, **MoodShift** allows you to seamlessly transition between moods and find music that resonates with how you feel right now.

Simply select your desired mood—whether it’s upbeat, intense, calm, or introspective—and let **MoodShift** suggest the best tracks to elevate or complement your state of mind. From the latest hits to hidden gems, we curate your experience to ensure the perfect playlist for every vibe.

Shift your mood, explore new music, and enjoy the power of sound with **MoodShift**!
         """)

st.logo(
    "1.png",
    icon_image="3.png",
    size="large"
    )

st.sidebar.write("Welcome to MoodShift, the ultimate music experience that tunes into your emotions and shifts your vibe to match any mood. Whether you're feeling energetic, calm, intense, or reflective, MoodShift helps you discover the perfect soundtrack for every moment.")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/4/48/Foreigner_-_Agent_Provocateur.JPG", use_column_width=True)
st.sidebar.write("With MoodShift, we’ve analyzed key musical attributes like energy, danceability, tempo, and emotional tone to categorize songs into distinct 'mood clusters.' Whether you’re looking to get lost in high-energy beats or relax with mellow acoustic sounds, MoodShift allows you to seamlessly transition between moods and find music that resonates with how you feel right now.")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/8/8f/Rainbow_-_Ritchie_Blackmore%27s_Rainbow_%281975%29_front_cover.jpg", use_column_width=True)
mapping = {
    0 : "Energetic and Danceable",
    1 : "Calm and Reflective",
    2 : "Dark and Intense",
    3 : "Emotional and Somber"
}

import pandas as pd

df = pd.read_csv("data_with_clusters.csv")
df = df.dropna(subset=['preview_url'])
df = df.dropna(subset=['url'])
df['mood_text'] = df['mood'].map(mapping)


tab2.dataframe(df)


# Calculate summary metrics for the selected mood
avg_popularity = df['popularity'].mean()
avg_danceability = df['danceability'].mean()
avg_energy = df['energy'].mean()
avg_tempo = df['tempo'].mean()

# Display Cards
col1, col2, col3, col4 = tab2.columns(4)
col1.metric("Average Popularity", f"{avg_popularity:.2f}")
col2.metric("Average Danceability", f"{avg_danceability:.2f}")
col3.metric("Average Energy", f"{avg_energy:.2f}")
col4.metric("Average Tempo", f"{avg_tempo:.2f} BPM")

# Display filtered table

# Create interactive graphs using Plotly
tab2.subheader("Key Attributes for Selected Mood")

# Scatter plot for Energy vs Danceability
fig1 = px.scatter(df, x='energy', y='danceability', color='popularity',
                  hover_data=['name', 'artist'], title="Energy vs Danceability")
tab2.plotly_chart(fig1, use_container_width=True)

# Histogram for Popularity Distribution
fig2 = px.histogram(df, x='energy', nbins=10, title="Popularity Distribution")
tab2.plotly_chart(fig2, use_container_width=True)



















user_selected_mood = tab3.selectbox("Select your mood", options= df['mood_text'].unique())

if tab3.button("Suggest Song", key="suggest_song", use_container_width=True, icon="🎵"):
    col1, col2, col3, col4, col5 = tab3.columns(5)
    suggested_songs = df[df['mood_text'] == user_selected_mood]
    for col in [col1, col2, col3, col4, col5]:
        song = suggested_songs.sample(n=1)
        col.image(song['url'].values[0], use_column_width=True)
        col.write(song['artist'].values[0])
        col.write(song['name'].values[0])
        if song['preview_url'].values[0]:
            col.audio(song['preview_url'].values[0])
            
            