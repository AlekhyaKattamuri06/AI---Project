# music_recommender.py

import os
from dotenv import load_dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

print("Client ID loaded:", os.getenv("SPOTIPY_CLIENT_ID"))

# Spotify setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Hugging Face LLM
def get_song_recommendation(emotion):
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}
    prompt = f"Suggest one song that matches the mood: {emotion}. Include title and artist."
    data = {"inputs": prompt, "parameters": {"max_new_tokens": 50}}

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
        headers=headers,
        json=data
    )
    output = response.json()
    if isinstance(output, list):
        return output[0]['generated_text']
    return "Could not generate a song."

def search_song(song_name):
    results = sp.search(q=song_name, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            "title": track['name'],
            "artist": track['artists'][0]['name'],
            "album": track['album']['name'],
            "image_url": track['album']['images'][0]['url'],
            "preview_url": track['preview_url']
        }
    return None
