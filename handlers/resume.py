from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import get_queue

# Command to resume playback
@Client.on_message(filters.command("resume") & filters.group)
async def resume_command(client: Client, message: Message):
    chat_id = message.chat.id
    queue = await get_queue(chat_id)

    if not queue:
        await message.reply("No music is currently paused to resume.")
        return

    # Logic to resume the playback (using Py-TgCalls)
    await client.send_message(chat_id, "Playback has been resumed.")