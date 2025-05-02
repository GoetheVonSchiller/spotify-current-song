# Spotify Currently Playing Tracker

This project is a Python script that monitors the currently playing song of a Spotify user and outputs information about the song. It uses the Spotify Web API and the `spotipy` library for authentication and data retrieval.

## Prerequisites

Before running the script, ensure the following prerequisites are met:

1. **Spotify Developer Account**: Create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to obtain the `CLIENT_ID` and `CLIENT_SECRET`.
2. **Libraries**: Install the required Python libraries:
   ```bash
   pip install spotipy requests
   ```

## Setup

1. **Spotify API Credentials**: Replace the following variables in the script with your own credentials:
   ```python
   CLIENT_ID = "your_client_id"
   CLIENT_SECRET = "your_client_secret"
   REDIRECT_URI = "http://localhost:8888"
   ```

2. **Permissions**: The script uses the `user-read-currently-playing` scope to access the currently playing song. Ensure this scope is enabled in your Spotify application.

## How It Works

### 1. **Authentication**
The script uses `SpotifyOAuth` from the `spotipy` library to authenticate the user and obtain an access token.

### 2. **Token Refresh**
The `refresh_access_token` function automatically refreshes the access token when it expires (after 1 hour).

### 3. **Fetching the Current Song**
The `get_current_track` function retrieves the currently playing song via the Spotify Web API and returns details such as song ID, name, artists, and Spotify link.

### 4. **Monitoring**
The `main` function continuously monitors the currently playing song and outputs the information when the song changes.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The script outputs information about the currently playing song, e.g.:
   ```
   {'id': '12345', 'track_name': 'Song Name', 'artists': 'Artist Name', 'link': 'https://open.spotify.com/track/12345'}
   ```

## Notes

- **API Limits**: The script fetches data from the Spotify API every 5 seconds to avoid exceeding API rate limits.