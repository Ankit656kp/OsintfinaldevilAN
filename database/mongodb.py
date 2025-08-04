from motor.motor_asyncio import AsyncIOMotorClient
import os

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "uploadbot")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Collection for uploaded parsed data
data_col = db["uploads"]