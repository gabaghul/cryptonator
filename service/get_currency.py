from datetime import datetime
import json
from typing import Tuple
import requests
from commons.mapping import get_currency_name

from consts import CURRENCY_INDEX, ENDPOINT_CURRENCY_VALUE, RAPIDAPI_APPKEY, COINGECKO_HOST, ENDPOINT_SUPPORTED_CURRENCIES

def get_supported_currencies() -> Tuple[list, int]:
    url = COINGECKO_HOST + ENDPOINT_SUPPORTED_CURRENCIES

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_APPKEY
    }

    response = requests.request("GET", url, headers=headers)
    
    return json.dumps(response.json()), response.status_code

def get_currency_value(symbol: str, currency_index: str) -> Tuple[dict, int]:
    url = COINGECKO_HOST + ENDPOINT_CURRENCY_VALUE

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_APPKEY
    }

    params= {
        'ids': get_currency_name(symbol),
        'vs_currencies': currency_index
    }

    response = requests.request("GET", url, headers=headers, params=params)

    history = response.json()
    history['date'] = datetime.now()
    
    return history, response.status_code
