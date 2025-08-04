import os

# Telegram API credentials
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with your actual API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:pass@cluster.mongodb.net/")
MONGO_DB_NAME = "devil_osint"

# Owner (admin) Telegram ID
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Support / Developer
DEV_USERNAME = "YourUsernameHere"
SUPPORT_GROUP = "https://t.me/your_support_group"