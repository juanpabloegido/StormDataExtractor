import os
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017/")
DB_NAME = "storm_data"
COLLECTION_NAME = "events"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
col = db[COLLECTION_NAME]
col.create_index("alert_id", unique=True)  # make alert_id unique to avoid duplicates

def get_events_collection():
    return col
