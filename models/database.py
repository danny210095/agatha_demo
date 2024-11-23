from pymongo import MongoClient
from config import MONGODB_URI

# 初始化 MongoDB 连接
class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client['Agatha']

    def get_collection(self, collection_name):
        return self.db[collection_name]

db = MongoDB()
