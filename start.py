import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="MoodShift", page_icon="🎵")
st.title(":orange[Mood]:blue[Shift] 🍃")
#st.image("1.png")

st.subheader("Discover the perfect soundtrack for every mood!")

home_tab, data_tab, recommendations_tab = st.tabs(["Home", "Data", "Recommendations"])

text_col, image_col_left, image_col_right = home_tab.columns([2,1,1], gap="small")

text_col.markdown("""

Welcome to **MoodShift**, the ultimate music experience that tunes into your emotions and shifts your vibe to match any mood. Whether you're feeling energetic, calm, intense, or reflective, **MoodShift** helps you discover the perfect soundtrack for every moment.

With **MoodShift**, we’ve analyzed key musical attributes like energy, danceability, tempo, and emotional tone to categorize songs into distinct "mood clusters." Whether you’re looking to get lost in high-energy beats or relax with mellow acoustic sounds, **MoodShift** allows you to seamlessly transition between moods and find music that resonates with how you feel right now.

Simply select your desired mood—whether it’s upbeat, intense, calm, or introspective—and let **MoodShift** suggest the best tracks to elevate or complement your state of mind. From the latest hits to hidden gems, we curate your experience to ensure the perfect playlist for every vibe.

Shift your mood, explore new music, and enjoy the power of sound with **MoodShift**!
         """)

image_col_left.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/19/JethroTullAqualungalbumcover.jpg/220px-JethroTullAqualungalbumcover.jpg", width=250)
image_col_right.image("https://upload.wikimedia.org/wikipedia/tr/3/3e/Graduation-album.jpg", width=250)
image_col_left.image("https://upload.wikimedia.org/wikipedia/en/3/35/The_Eminem_Show.jpg", width=250)
image_col_right.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/15/HatfulofHollow84.jpg/220px-HatfulofHollow84.jpg", width=250)

st.logo(
    image="1.png",
    icon_image="3.png",
    size="large"
    )

st.sidebar.write("Welcome to MoodShift, the ultimate music experience that tunes into your emotions and shifts your vibe to match any mood. Whether you're feeling energetic, calm, intense, or reflective, MoodShift helps you discover the perfect soundtrack for every moment.")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/4/48/Foreigner_-_Agent_Provocateur.JPG", use_column_width=True)
st.sidebar.write("With MoodShift, we’ve analyzed key musical attributes like energy, danceability, tempo, and emotional tone to categorize songs into distinct 'mood clusters.' Whether you’re looking to get lost in high-energy beats or relax with mellow acoustic sounds, MoodShift allows you to seamlessly transition between moods and find music that resonates with how you feel right now.")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/8/8f/Rainbow_-_Ritchie_Blackmore%27s_Rainbow_%281975%29_front_cover.jpg", use_column_width=True)


## Data Tab

mapping = {
    0 : "Energetic and Danceable",
    1 : "Calm and Reflective",
    2 : "Dark and Intense",
    3 : "Emotional and Somber"
}

@st.cache_data
def get_data():    
    df = pd.read_csv("data_with_clusters.csv")
    df = df.dropna(subset=['preview_url'])
    df = df.dropna(subset=['url'])
    df['mood_text'] = df['mood'].map(mapping)
    return df

df = get_data()
data_tab.dataframe(df)

avg_popularity = df['popularity'].mean()
avg_danceability = df['danceability'].mean()
avg_energy = df['energy'].mean()
avg_tempo = df['tempo'].mean().round(2)

col1, col2, col3, col4 = data_tab.columns(4)

col1.metric("Average Popularity", avg_popularity)
col2.metric("Average Danceability", avg_danceability)
col3.metric("Average Energy", avg_energy)
col4.metric("Average Tempo", avg_tempo)

fig1 = px.scatter(df,
                x="energy",
                y="danceability",
                color="mood_text",
                title="Energy vs Danceability",
                hover_data=["name", "artist"])

data_tab.plotly_chart(fig1)

# Histogram for Popularity Distribution
fig2 = px.histogram(df, x='energy', nbins=10, title="Popularity Distribution")
data_tab.plotly_chart(fig2, use_container_width=True)


## Recommendations Tab

user_selected_mood = recommendations_tab.selectbox("Select your mood", options= df.mood_text.unique())

if recommendations_tab.button("Suggest Songs", use_container_width=True, icon="🎵"):
    col1, col2, col3, col4, col5 = recommendations_tab.columns(5)
    suggestions = df[df['mood_text'] == user_selected_mood].sample(5)
    
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.image(suggestions['url'].values[i], use_column_width=True)
            st.write(suggestions['artist'].values[i])
            st.write(suggestions['name'].values[i])
            st.audio(suggestions['preview_url'].values[i])
        