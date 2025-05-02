import datetime
import time

import requests
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8888"
SCOPE = "user-read-currently-playing"


# Function to refresh the Spotify access token
def refresh_access_token(auth_manager):
    # Retrieve a new access token using the SpotifyOAuth manager
    access_token = auth_manager.get_access_token(as_dict=False)
    print("Access token refreshed")
    return access_token, datetime.datetime.now()


# Function to get the currently playing track from Spotify
def get_current_track(access_token):
    try:
        response = requests.get(
            'https://api.spotify.com/v1/me/player/currently-playing',
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        # No track is currently playing
        if response.status_code == 204:
            print("No track is currently playing.")
            return None

        # Error while fetching the track
        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        json_resp = response.json()

        # Extract track details such as ID, name, artists, and Spotify link
        track_id = json_resp["item"]["id"]
        track_name = json_resp["item"]["name"]
        artists = list(json_resp["item"]["artists"])
        artist_names = ", ".join([artist["name"] for artist in artists])
        link = json_resp["item"]["external_urls"]["spotify"]

        current_track_info = {
            "id": track_id,
            "track_name": track_name,
            "artists": artist_names,
            "link": link
        }

        return current_track_info
    except Exception as e:
        print(f"Error: {e}")
        return None


# Main function to monitor the currently playing track
def main():
    # Initialize the SpotifyOAuth manager
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )

    # Initialization
    access_token, last_refresh = refresh_access_token(auth_manager)
    current_track_id = None

    while True:
        try:
            # Refresh the access token if it has expired (after 1 hour)
            if (datetime.datetime.now() - last_refresh).seconds > 3600:
                access_token, last_refresh = refresh_access_token(auth_manager)

            # Fetch the currently playing track
            current_track = get_current_track(access_token)
            if current_track:
                # If the track has changed, update the current track ID and print the new track info
                if current_track_id != current_track["id"]:
                    current_track_id = current_track["id"]
                    print(current_track)

            # Wait for 5 seconds before checking again
            # This is to avoid hitting the API rate limit
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()
