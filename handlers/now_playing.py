from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import get_queue

# Command to display the currently playing song
@Client.on_message(filters.command("nowplaying") & filters.group)
async def now_playing(client: Client, message: Message):
    chat_id = message.chat.id
    queue = await get_queue(chat_id)

    if not queue:
        await message.reply("No music is currently playing.")
        return

    # Get the current song from the queue
    current_song = queue[0]
    
    # Create playback control buttons
    playback_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Pause", callback_data="pause"),
                InlineKeyboardButton("Resume", callback_data="resume"),
                InlineKeyboardButton("Skip", callback_data="skip"),
                InlineKeyboardButton("Stop", callback_data="stop"),
            ]
        ]
    )

    # Display the currently playing song with control buttons
    await message.reply_photo(
        photo=current_song["thumbnail"] or "https://via.placeholder.com/150",
        caption=f"🎵 **Now Playing:** {current_song['title']}\n"
                f"🎤 **Artist:** {current_song['artist']}",
        reply_markup=playback_markup,
    )