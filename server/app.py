from flask import Flask

import db.repository as repository

app = Flask(__name__)

@app.route("/")
def home():
    repository.insert_coin_history({"name": "BTC"})
    return "Hello Flask!!"

def start():
    app.run(host='0.0.0.0',port=5000)