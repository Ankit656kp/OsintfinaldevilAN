from pyrogram import filters
from pyrogram.types import Message
from bot import bot
from database.mongodb import users_col, data_col
from utils.helper import format_result, check_credits, deduct_credit

@bot.on_message(filters.text & filters.private)
async def aadhaar_lookup(client, message: Message):
    query = message.text.strip()

    # Only proceed if input is a valid 12-digit Aadhaar number
    if not (query.isdigit() and len(query) == 12):
        return

    user_id = message.from_user.id

    # Check user credits
    has_credit = await check_credits(user_id)
    if not has_credit:
        await message.reply("❌ You don't have enough credits.\nUse /addcredit or contact admin.")
        return

    # Find record by Aadhaar
    record = await data_col.find_one({"ADHAR": query})
    if record:
        await deduct_credit(user_id)
        await message.reply_text(format_result(record))
    else:
        await message.reply("⚠️ No record found for this Aadhaar number.")
