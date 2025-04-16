import os
from pyrogram import Client, idle
from pyrogram.enums import ParseMode
from pyrogram.types import Message

# Importing handlers
from handlers import play, queue, admin, stop, now_playing
from utils.database import init_db

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Initialize the Pyrogram client
app = Client(
    "MusicBot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
    plugins=dict(root="handlers"),
)

# Initialize the database
init_db()

# Start the bot
if __name__ == "__main__":
    print("Starting Telegram Music Bot...")
    app.start()
    print("Bot started successfully!")
    idle()
    app.stop()
    print("Bot stopped.")