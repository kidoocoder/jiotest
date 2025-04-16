from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

about = "https://t.me/yOur_DadDy_vIcky"
help = "https://t.me/yOur_DadDy_vIcky"
# Command to handle /start in private or group
@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    # Check if the command is sent in a private chat or group
    if message.chat.type == "private":
        # Message for private chats
        text = (
            "👋 Hello! I'm your **Music Bot**.\n\n"
            "🎶 I can help you play music in your groups' voice chats. "
            "Use the buttons below to get started!"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add Me To Your Group", url="https://t.me/vickyspotifyrobot?startgroup=true"),
                ],
                [
                    InlineKeyboardButton("📜 Help & Commands", callback_data="help"),
                    InlineKeyboardButton("ℹ️ About", callback_data="about"),
                ]
            ]
        )
    else:
        # Message for groups
        text = (
            "👋 Hello! I'm your **Music Bot**.\n\n"
            "🎶 Use /play <song name> to start playing music in this group."
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📜 Help & Commands", callback_data="help"),
                ]
            ]
        )

    # Send the message with buttons
    await message.reply(
        text,
        reply_markup=reply_markup,
    )