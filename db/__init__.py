import pymongo
from consts import MONGO_URI, MONGO_PORT

class MongoManager:
    def __init__(self, client=None):
        self.client = pymongo.MongoClient(MONGO_URI, MONGO_PORT)

client = MongoManager().client