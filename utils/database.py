from motor.motor_asyncio import AsyncIOMotorClient
import os

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = mongo_client["telegram_music_bot"]

# Collections for queues and playlists
queue_collection = db["queues"]
playlist_collection = db["playlists"]

async def init_db():
    """
    Initializes the database by creating necessary collections and indexes.
    """
    await queue_collection.create_index("chat_id", unique=True)
    await playlist_collection.create_index("chat_id", unique=True)

# Queue-related operations
async def add_to_queue(chat_id: int, song: dict):
    """
    Adds a song to the queue for a specific chat.
    :param chat_id: Telegram chat ID.
    :param song: Dictionary containing song details.
    """
    await queue_collection.update_one(
        {"chat_id": chat_id},
        {"$push": {"queue": song}},
        upsert=True
    )

async def get_queue(chat_id: int):
    """
    Retrieves the queue for a specific chat.
    :param chat_id: Telegram chat ID.
    :return: List of songs in the queue.
    """
    chat_data = await queue_collection.find_one({"chat_id": chat_id})
    return chat_data["queue"] if chat_data and "queue" in chat_data else []

async def remove_from_queue(chat_id: int):
    """
    Removes the first song from the queue for a specific chat.
    :param chat_id: Telegram chat ID.
    """
    await queue_collection.update_one(
        {"chat_id": chat_id},
        {"$pop": {"queue": -1}}  # Remove the first item in the queue
    )

async def clear_queue(chat_id: int):
    """
    Clears the queue for a specific chat.
    :param chat_id: Telegram chat ID.
    """
    await queue_collection.delete_one({"chat_id": chat_id})

# Playlist-related operations
async def save_playlist(chat_id: int, playlist: list):
    """
    Saves a playlist for a specific chat.
    :param chat_id: Telegram chat ID.
    :param playlist: List of songs to save as a playlist.
    """
    await playlist_collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"playlist": playlist}},
        upsert=True
    )

async def get_playlist(chat_id: int):
    """
    Retrieves the playlist for a specific chat.
    :param chat_id: Telegram chat ID.
    :return: List of songs in the playlist.
    """
    chat_data = await playlist_collection.find_one({"chat_id": chat_id})
    return chat_data["playlist"] if chat_data and "playlist" in chat_data else []

async def clear_playlist(chat_id: int):
    """
    Clears the playlist for a specific chat.
    :param chat_id: Telegram chat ID.
    """
    await playlist_collection.delete_one({"chat_id": chat_id})