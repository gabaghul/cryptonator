_symbol_to_name = {
    'btc': 'bitcoin'
}

def get_currency_name(symbol: str) -> str :
    return _symbol_to_name.get(symbol)