from pyrogram import filters
from pyrogram.types import Message
from main import bot
from config import OWNER_ID
from utils.parser import parse_uploaded_file
from database.mongodb import data_col
import os
import aiofiles

@bot.on_message(filters.command("upload") & filters.user(OWNER_ID))
async def handle_upload(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("📎 Reply to a ZIP, TXT, or JSON file with `/upload`.")
        return

    file = message.reply_to_message.document
    file_ext = file.file_name.split(".")[-1].lower()

    if file_ext not in ["zip", "txt", "json"]:
        await message.reply("❌ Unsupported file format.")
        return

    path = f"uploads/{file.file_name}"
    await message.reply("📥 Downloading file...")

    await client.download_media(message.reply_to_message, file_name=path)

    # Parse the data
    await message.reply("📊 Parsing and importing data...")
    records = await parse_uploaded_file(path)

    if not records:
        await message.reply("⚠️ No valid records found in the file.")
        return

    # Insert into DB
    await data_col.insert_many(records)
    await message.reply(f"✅ Uploaded and added {len(records)} records to database.")

    # Delete temp file
    os.remove(path)