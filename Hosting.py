import streamlit as st
import requests

st.set_page_config(page_title="Mood Mirror", layout="centered")

st.title("🎧 Mood Mirror")
st.write("Upload a selfie or use your webcam to detect your mood and get a matching song 🎵")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
webcam_image = st.camera_input("Or take a photo")

image = uploaded_file or webcam_image

def get_emotion_and_song(image_bytes):
    # Stub for testing — replace with real function or API call
    return {
        "emotion": "happy",
        "song": {
            "name": "Happy",
            "artist": "Pharrell Williams",
            "album_art": "https://link_to_art.jpg",
            "preview_url": "https://link_to_preview.mp3"
        }
    }
if image:
    with st.spinner("Analyzing..."):
        bytes_data = image.getvalue()
        result = get_emotion_and_song(bytes_data)

        st.subheader(f"Detected Emotion: 😄 {result['emotion'].capitalize()}")
        song = result["song"]
        st.markdown(f"**{song['name']}** by *{song['artist']}*")
        st.image(song["album_art"], width=200)
        st.audio(song["preview_url"], format="audio/mp3")
st.markdown("---")
if st.button("Try another image"):
    st.experimental_rerun()

# app.py
import streamlit as st

st.title("Emotion-Based Song Recommender")
st.write("Hello! This is Mainuddin's Streamlit UI 😊")
