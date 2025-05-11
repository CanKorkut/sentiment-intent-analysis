from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["conversation_analysis"]
collection = db["logs"]

async def log_analysis(data: dict):
    data["timestamp"] = datetime.utcnow()
    await collection.insert_one(data)
