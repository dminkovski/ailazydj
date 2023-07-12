import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

redirect_uri = 'http://localhost:8080'
scope = 'user-modify-playback-state'

class SpotifyClient:
    def main(self):
        SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        #auth_manager = SpotifyClientCredentials( client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
        return spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=redirect_uri))
