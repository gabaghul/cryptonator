from envyaml import EnvYAML

env = EnvYAML('config.yml', strict=False)

# MONGO
MONGO_URI = env['mongo']['uri']
MONGO_PORT = env['mongo']['port']

# RAPIDAPI APP KEY
RAPIDAPI_APPKEY = env['appkey']

# COINGECKO API HOST
COINGECKO_HOST = env['coingecko']['host']

# COINGECKO API RESOURCES
ENDPOINT_SUPPORTED_CURRENCIES = env['coingecko']['resources']['supported_currencies']
ENDPOINT_CURRENCY_VALUE = env['coingecko']['resources']['simple_price']

# ANALYZED COIN
COIN_SYMBOL = 'btc'

# CURRENCY COMPARISON INDEX
CURRENCY_INDEX = 'usd'