from . import MongoManager
def insert_coin_history(history: dict) -> bool:
    client = MongoManager.client
    db = client['cryptocoins']
    collection = db['history']

    collection.insert_one(history)
