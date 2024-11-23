from models.database import db
from config import BOT_CONFIG, DEFAULT_MODE

class UserContextManager:
    def __init__(self):
        self.user_collection = db.get_collection('UserSettings')

    def save_user_mode(self, group_id, user_id, mode):
        self.user_collection.update_one(
            {"groupId": group_id, "userId": user_id},
            {"$set": {"mode": mode}},
            upsert=True
        )

    def get_user_mode(self, group_id, user_id):
        record = self.user_collection.find_one({"groupId": group_id, "userId": user_id})
        return record.get("mode", DEFAULT_MODE) if record else DEFAULT_MODE

    def save_chat_history(self, topic, user_id, message):
        collection_name = BOT_CONFIG[topic]["collection"]
        collection = db.get_collection(collection_name)
        collection.insert_one({"userId": user_id, "text": message})

    def get_chat_history(self, topic, user_id):
        collection_name = BOT_CONFIG[topic]["collection"]
        collection = db.get_collection(collection_name)
        return [doc['text'] for doc in collection.find({"userId": user_id}).sort("_id", -1).limit(10)]

