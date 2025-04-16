from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import get_queue, remove_from_queue

# Command to skip the current song
@Client.on_message(filters.command("skip") & filters.group)
async def skip_command(client: Client, message: Message):
    chat_id = message.chat.id
    queue = await get_queue(chat_id)

    if not queue:
        await message.reply("No music is currently playing to skip.")
        return

    # Remove the current song from the queue
    await remove_from_queue(chat_id)

    # Play the next song in the queue (if available)
    queue = await get_queue(chat_id)
    if queue:
        next_song = queue[0]
        await message.reply(f"Skipped to the next song: {next_song['title']} by {next_song['artist']}")
    else:
        await message.reply("Queue is empty. Stopping playback.")