import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
from beanie import init_beanie
from models.model import User, Message

# Import Mongo URI
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

async def init_db():
    client = AsyncMongoClient(MONGO_URI)
    await init_beanie(database=client.db_name, document_models=[User, Message])