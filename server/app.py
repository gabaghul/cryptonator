from flask import Flask

import db

app = Flask(__name__)

@app.route("/")
def home():
    db.insert_coin_history({"name": "BTC"})
    print('test')
    return "Hello Flask!!"

@app.route("/insert")
def insert():
    db.insert_coin_history({"name": "BTC"})

def start():
    app.run(host='0.0.0.0',port=5000)