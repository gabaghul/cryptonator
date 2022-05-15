from flask import Flask

import db.repository as repository
import service.get_currency as service

app = Flask(__name__)

@app.route("/")
def home():
    # repository.insert_coin_history({"name": "BTC"})
    return "Hello Flask!!"

@app.route("/supported-currencies")
def supported_currencies():
    return service.get_supported_currencies()

def start():
    app.run(host='0.0.0.0',port=5000)