from pymongo import MongoClient
import src.config as config
print(config.MONGO_URI)
client = MongoClient(config.MONGO_URI)

db = client.money_tracker_site_db

collection_name = db["blog_collection"]