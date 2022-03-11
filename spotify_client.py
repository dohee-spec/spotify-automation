import requests
from tokens import *
from datetime import datetime
import datetime

SPOTIFY_API = "https://api.spotify.com"

class SpotifyClient(object):
    def __init__(self) -> None:
        pass

    def get_recent_tracks(self, limit, hours):
        # Convert time to Unix timestamp in miliseconds      
        now = datetime.datetime.now()
        ago = now - datetime.timedelta(hours = hours)
        ago_unix_timestamp = int(ago.timestamp()) * 1000
        time = ago_unix_timestamp

        headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/json",
            "Authorization" : f"Bearer {access_token_recent}"
            }

        # Request API endpoint
        endpoint = "/v1/me/player/recently-played"
        url=f"{SPOTIFY_API}{endpoint}?limit={limit}&after={time}"
        r = requests.get(url, headers = headers)
        
        return r.json()

    def remove_playlist_items(self):
        pass

    def add_playlist_items(self):
        pass

    def create_playlist(self):
        pass

    def add_playlist_image(self):
        pass

    def update_playlist(self):
        pass

    def change_playlist_details(self):
        pass