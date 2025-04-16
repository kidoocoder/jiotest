import aiohttp

BASE_URL = "https://api-v2.soundcloud.com"
CLIENT_ID = "YOUR_SOUNDCLOUD_CLIENT_ID"  # Replace this with your SoundCloud client ID

async def get_song_from_soundcloud(query: str):
    """
    Search and fetch song details from SoundCloud.
    :param query: Song name or artist to search for.
    :return: Dictionary containing song details or None if not found.
    """
    search_url = f"{BASE_URL}/search/tracks?q={query}&client_id={CLIENT_ID}"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            if response.status == 200:
                data = await response.json()
                if data["collection"]:
                    track = data["collection"][0]
                    return {
                        "title": track["title"],
                        "artist": track["user"]["username"],
                        "url": track["permalink_url"],
                        "duration": track["duration"] // 1000,  # Convert to seconds
                        "thumbnail": track["artwork_url"],
                    }
    return None