#FastApiStudy\app\database\mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
mongo_db = client[settings.MONGO_DB_NAME]
todo_collection = mongo_db.get_collection("todos")