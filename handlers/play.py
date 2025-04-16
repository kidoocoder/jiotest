from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from utils.jiosaavn import get_song_from_jiosaavn
from utils.spotify import get_song_from_spotify
from utils.soundcloud import get_song_from_soundcloud
from utils.resso import get_song_from_resso
from utils.database import add_to_queue, get_queue
from pyrogram.types import Message

# Command to play music
@Client.on_message(filters.command("play") & filters.group)
async def play_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("Please specify the name of the song to play.")
        return

    # Search for the song in JioSaavn
    song = await get_song_from_jiosaavn(query)
    if not song:
        # If not found, fallback to Spotify
        song = await get_song_from_spotify(query)
    if not song:
        # If not found on Spotify, fallback to SoundCloud
        song = await get_song_from_soundcloud(query)
    if not song:
        # If not found on SoundCloud, fallback to Resso
        song = await get_song_from_resso(query)
    if not song:
        await message.reply("Sorry, I couldn't find the song on any platform.")
        return

    # Add song to queue
    add_to_queue(message.chat.id, song)

    # Display playback controls
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

    await message.reply(
        f"Now playing: {song['title']} by {song['artist']}",
        reply_markup=playback_markup,
    )


# Callback query handler for playback controls
@Client.on_callback_query(filters.regex("^(pause|resume|skip|stop)$"))
async def playback_controls(client: Client, callback_query: CallbackQuery):
    action = callback_query.data
    chat_id = callback_query.message.chat.id

    if action == "pause":
        await callback_query.message.reply("Paused playback.")
    elif action == "resume":
        await callback_query.message.reply("Resumed playback.")
    elif action == "skip":
        queue = get_queue(chat_id)
        if len(queue) > 1:
            queue.pop(0)  # Remove the current song from the queue
            await callback_query.message.reply(f"Skipped to: {queue[0]['title']}")
        else:
            await callback_query.message.reply("Queue is empty. Stopping playback.")
    elif action == "stop":
        await callback_query.message.reply("Stopped playback.")