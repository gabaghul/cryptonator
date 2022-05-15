from db import client


def insert_coin_history(history: dict) -> bool:
    db = client['cryptocoins']
    collection = db['history']

    return collection.insert_one(history)