import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Spotify client
spotify_client = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    )
)

async def get_song_from_spotify(query: str):
    """
    Search and fetch song details from Spotify.
    :param query: Song name or artist to search for.
    :return: Dictionary containing song details or None if not found.
    """
    try:
        results = spotify_client.search(q=query, type="track", limit=1)
        if results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            return {
                "title": track["name"],
                "artist": ", ".join([artist["name"] for artist in track["artists"]]),
                "url": track["external_urls"]["spotify"],
                "duration": track["duration_ms"] // 1000,  # Convert to seconds
                "thumbnail": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
            }
    except Exception as e:
        print(f"Error fetching song from Spotify: {e}")
    return None