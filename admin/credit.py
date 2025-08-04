from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from main import bot
from database.mongodb import db

@bot.on_message(filters.command("addcredit") & filters.user(OWNER_ID))
async def add_credit(_, message: Message):
    if len(message.command) < 3:
        return await message.reply("❌ Usage: `/addcredit user_id amount`", quote=True)

    try:
        user_id = int(message.command[1])
        amount = int(message.command[2])
    except ValueError:
        return await message.reply("❌ Invalid input. Both user_id and amount must be numbers.", quote=True)

    user = db.users.find_one({"user_id": user_id})
    if not user:
        return await message.reply("⚠️ User not found in database.", quote=True)

    new_credit = user.get("credits", 0) + amount
    db.users.update_one({"user_id": user_id}, {"$set": {"credits": new_credit}})

    await message.reply(f"✅ Added `{amount}` credits to `{user_id}`.\n💳 New balance: `{new_credit}`", quote=True)


@bot.on_message(filters.command("setcredit") & filters.user(OWNER_ID))
async def set_credit(_, message: Message):
    if len(message.command) < 3:
        return await message.reply("❌ Usage: `/setcredit user_id amount`", quote=True)

    try:
        user_id = int(message.command[1])
        amount = int(message.command[2])
    except ValueError:
        return await message.reply("❌ Invalid input. Both user_id and amount must be numbers.", quote=True)

    user = db.users.find_one({"user_id": user_id})
    if not user:
        return await message.reply("⚠️ User not found in database.", quote=True)

    db.users.update_one({"user_id": user_id}, {"$set": {"credits": amount}})
    await message.reply(f"✅ Set credits of `{user_id}` to `{amount}`.", quote=True)