from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import start_menu, lookup_phone, lookup_aadhaar, menu_buttons
from admin import upload, credit, broadcast, stats

import os
import asyncio

# Bot instance
bot = Client(
    "devil-osint-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=100,
    plugins={"root": "."}
)

# Run the bot
if __name__ == "__main__":
    print("🔥 Devil OSINT Bot starting...")
    bot.run()