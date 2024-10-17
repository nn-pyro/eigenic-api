from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
DB_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB")
API_KEY = os.getenv("OPENAI_API_KEY")

DATABASE = MongoClient(DB_URI)[DB_NAME]

__all__ = [DATABASE]