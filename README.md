# Telegram Music Bot

A full-featured Telegram music bot that streams music into group voice chats using Pyrogram and Py-TgCalls. The bot supports JioSaavn, Spotify, SoundCloud, and Resso as music sources.

## Features
- `/play` command with inline search
- `/pause`, `/resume`, `/skip`, `/stop`
- Playlist support per group
- Auto-leave from inactive voice chats
- Admin-only control toggle
- Now playing display with control buttons
- Queue management
- Lightweight UI with playback thumbnails

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- MongoDB database

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/syntaxworldcodes/telegram_music_bot.git
   cd telegram_music_bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env` and fill in the required values.

4. Start the bot:
   ```bash
   python main.py
   ```

### Deployment
- Deployable on Heroku or any Linux VPS.
- Include the `Procfile` for Heroku:
   ```plaintext
   worker: python main.py
   ```

Enjoy your music bot!