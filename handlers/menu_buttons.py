from pyrogram import filters
from pyrogram.types import CallbackQuery
from bot import bot

@bot.on_callback_query(filters.regex("phone_lookup"))
async def phone_lookup_handler(client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "📞 *Phone Lookup*\n\nSend the phone number (10 digits) you'd like to search.",
        reply_markup=None
    )

@bot.on_callback_query(filters.regex("aadhaar_lookup"))
async def aadhaar_lookup_handler(client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "🆔 *Aadhaar Lookup*\n\nSend the Aadhaar number (12 digits) you'd like to search.",
        reply_markup=None
    )
