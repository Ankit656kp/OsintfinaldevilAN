from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from main import bot
from database.mongodb import db
from pyrogram.errors import FloodWait, PeerIdInvalid
import asyncio

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to the message you want to broadcast.")

    sent = 0
    failed = 0
    users = db.users.find({})
    msg = message.reply_to_message

    await message.reply("📣 Broadcast started...")

    async for user in users:
        try:
            await msg.copy(chat_id=user["user_id"])
            sent += 1
            await asyncio.sleep(0.05)  # prevent flood
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except PeerIdInvalid:
            failed += 1
        except:
            failed += 1

    await message.reply(f"✅ Broadcast finished.\n\n👥 Sent: `{sent}`\n❌ Failed: `{failed}`")