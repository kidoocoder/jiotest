from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import clear_queue

# Command to stop playback
@Client.on_message(filters.command("stop") & filters.group)
async def stop_command(client: Client, message: Message):
    chat_id = message.chat.id

    # Clear the music queue for the chat
    await clear_queue(chat_id)

    # Logic to stop the playback (using Py-TgCalls)
    await client.send_message(chat_id, "Playback has been stopped, and the queue has been cleared.")