from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import save_playlist, get_playlist, clear_playlist

# Command to save the current queue as a playlist
@Client.on_message(filters.command("saveplaylist") & filters.group)
async def save_playlist_command(client: Client, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        await message.reply("Please provide a name for the playlist. Usage: /saveplaylist <playlist_name>")
        return

    playlist_name = message.command[1]
    queue = await get_playlist(chat_id)

    if not queue:
        await message.reply("There's nothing in the queue to save as a playlist.")
        return

    await save_playlist(chat_id, queue)
    await message.reply(f"The playlist '{playlist_name}' has been saved successfully!")

# Command to list all saved playlists
@Client.on_message(filters.command("playlists") & filters.group)
async def list_playlists(client: Client, message: Message):
    chat_id = message.chat.id
    playlist = await get_playlist(chat_id)

    if not playlist:
        await message.reply("No playlists are saved for this group.")
        return

    playlists_list = "\n".join([f"- {song['title']} by {song['artist']}" for song in playlist])
    await message.reply(f"Saved Playlists:\n{playlists_list}")

# Command to clear the saved playlist
@Client.on_message(filters.command("clearplaylist") & filters.group)
async def clear_playlist_command(client: Client, message: Message):
    chat_id = message.chat.id

    await clear_playlist(chat_id)
    await message.reply("The playlist has been cleared.")