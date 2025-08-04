from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import DEV_USERNAME, SUPPORT_GROUP
from main import bot
from database.mongodb import users_col

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    user_id = message.from_user.id

    # Add user to DB if not exists
    user = await users_col.find_one({"user_id": user_id})
    if not user:
        await users_col.insert_one({
            "user_id": user_id,
            "credits": 0,
            "joined": str(message.date.date())
        })

    # Buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Phone Lookup", callback_data="phone_lookup")],
        [InlineKeyboardButton("🆔 Aadhaar Lookup", callback_data="aadhaar_lookup")],
        [
            InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/{DEV_USERNAME}"),
            InlineKeyboardButton("📢 Support Group", url=SUPPORT_GROUP)
        ]
    ])

    await message.reply_text(
        "**👋 Welcome to Devil OSINT Bot!**\n\n"
        "🔍 Use the buttons below to lookup Phone Numbers or Aadhaar Numbers.\n"
        "💳 You need credits to use these tools. Contact developer to get credits.",
        reply_markup=keyboard
    )