import aiohttp

BASE_URL = "https://jiosaavn-api-unofficial.vercel.app"

async def get_song_from_jiosaavn(query: str):
    """
    Search and fetch song details from JioSaavn.
    :param query: Song name or artist to search for.
    :return: Dictionary containing song details or None if not found.
    """
    search_url = f"{BASE_URL}/search?query={query}"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            if response.status == 200:
                data = await response.json()
                if "results" in data and len(data["results"]) > 0:
                    # Extract the first song from results
                    song_data = data["results"][0]
                    return {
                        "title": song_data["title"],
                        "artist": song_data["primary_artists"],
                        "url": song_data["media_url"],
                        "duration": song_data["duration"],
                        "thumbnail": song_data["image"],
                    }
    return None