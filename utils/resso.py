import aiohttp

BASE_URL = "https://resso-api-placeholder.example.com"  # Replace with a real Resso API endpoint

async def get_song_from_resso(query: str):
    """
    Search and fetch song details from Resso.
    :param query: Song name or artist to search for.
    :return: Dictionary containing song details or None if not found.
    """
    search_url = f"{BASE_URL}/search?q={query}"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            if response.status == 200:
                data = await response.json()
                if "results" in data and len(data["results"]) > 0:
                    track = data["results"][0]
                    return {
                        "title": track["name"],
                        "artist": track["artist"],
                        "url": track["url"],
                        "duration": track["duration"],
                        "thumbnail": track["thumbnail"],
                    }
    return None