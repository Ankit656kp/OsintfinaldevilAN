from pyrogram import filters
from pyrogram.types import Message
from main import bot
from database.mongodb import users_col, data_col
from utils.helper import format_result, check_credits, deduct_credit

@bot.on_message(filters.text & filters.private)
async def phone_number_lookup(client, message: Message):
    query = message.text.strip()

    # Only proceed if input is a valid 10-digit number
    if not (query.isdigit() and len(query) == 10):
        return

    user_id = message.from_user.id

    # Check user credits
    has_credit = await check_credits(user_id)
    if not has_credit:
        await message.reply("❌ You don't have enough credits.\nUse /addcredit or contact admin.")
        return

    # Find record by number
    record = await data_col.find_one({"NUMBER": query})
    if record:
        await deduct_credit(user_id)
        await message.reply_text(format_result(record))
    else:
        await message.reply("⚠️ No record found for this phone number.")