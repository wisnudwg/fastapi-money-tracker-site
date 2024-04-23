from pymongo import MongoClient
import src.config as config

client = MongoClient(config.CLIENT_URI)

db = client.fastapi_money_tracker_site_db

collection_name = db["blog_collection"]