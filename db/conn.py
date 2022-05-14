from . import MONGO_URI, MONGO_PORT
import pymongo

class MongoManager:
    class __MongoManager:
        def __init__(self):
            # Initialise mongo client
            self.client = pymongo.MongoClient(MONGO_URI, MONGO_PORT)

    __instance = None

    def __init__(self):
        if not MongoManager.__instance:
            MongoManager.__instance = MongoManager.__MongoManager()

    def __getattr__(self, item):
        return getattr(self.__instance, item)
