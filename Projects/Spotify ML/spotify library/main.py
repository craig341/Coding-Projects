import spotipy
from spotipy.oauth2 import SpotifyOAuth

# TARGET_PLAYLIST_ID = '17Pz7Z3X7MuBbbKyTXcrcM'
# CLIENT_ID = '41480b21a5a6447ebacdc35a02758962'
# CLIENT_SECRET = '6d9c27d967b34728b49b0dc0dbe476dd'
# REDIRECT_URI = 'http://localhost:8888/callback'
# SCOPE = 'playlist-read-private playlist-modify-private playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='41480b21a5a6447ebacdc35a02758962',
    client_secret="6d9c27d967b34728b49b0dc0dbe476dd",
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-modify-public"
))


def add_song_to_playlist(playlist_id, track_uri):
    try:
        sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])
        print("Song added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    playlist_id = "41ghPWQjuJb2GKUWq1rZDa"

    track_uri = "spotify:track:0nj9Bq5sHDiTxSHunhgkFb"

    for _ in range(1):
        add_song_to_playlist(playlist_id, track_uri)
