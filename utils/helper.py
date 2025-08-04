from database.mongodb import users_col

# ✅ Check if user has at least 1 credit
async def check_credits(user_id: int) -> bool:
    user = await users_col.find_one({"user_id": user_id})
    return user and user.get("credits", 0) > 0

# ➖ Deduct 1 credit
async def deduct_credit(user_id: int):
    await users_col.update_one(
        {"user_id": user_id},
        {"$inc": {"credits": -1}}
    )

# 🧾 Format the result nicely
def format_result(data: dict) -> str:
    return (
        f"**🔍 OSINT Record Found:**\n\n"
        f"👤 Name: `{data.get('NAME', 'N/A')}`\n"
        f"👨‍👦 Father Name: `{data.get('FNAME', 'N/A')}`\n"
        f"📍 Address: `{data.get('ADDRESS', 'N/A')}`\n"
        f"📱 Number: `{data.get('NUMBER', 'N/A')}`\n"
        f"🆔 Aadhaar: `{data.get('ADHAR', 'N/A')}`\n"
        f"📧 Email: `{data.get('EMAIL', 'N/A')}`"
    )