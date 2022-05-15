import json
from typing import Tuple
import requests

from consts import RAPIDAPI_APPKEY, COINGECKO_HOST, ENDPOINT_SUPPORTED_CURRENCIES

def get_supported_currencies() -> Tuple[list, int]:
    url = COINGECKO_HOST + ENDPOINT_SUPPORTED_CURRENCIES

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_APPKEY
    }

    response = requests.request("GET", url, headers=headers)
    
    return json.dumps(response.json()), response.status_code