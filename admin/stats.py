from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from main import bot
from database.mongodb import db

@bot.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def show_stats(_, message: Message):
    users = await db.users.count_documents({})
    total_uploads = await db.uploads.count_documents({})
    total_credits = await db.users.aggregate([{"$group": {"_id": None, "total": {"$sum": "$credits"}}}]).to_list(length=1)

    total_credits_value = total_credits[0]['total'] if total_credits else 0

    text = (
        "**📊 Bot Statistics:**\n\n"
        f"👤 Total Users: `{users}`\n"
        f"📥 Uploaded Combos/Items: `{total_uploads}`\n"
        f"💰 Total Credits in System: `{total_credits_value}`"
    )
    await message.reply(text)