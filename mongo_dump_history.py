import pandas as pd
from db.repository import insert_coin_history

df_btc_hour = pd.read_csv('bitcoin_load.csv')

for index, row in df_btc_hour.iterrows():
    history = {
        'bitcoin': {
            'usd': row['close']
        },
        'date': row['date']
    }

    insert_ok = insert_coin_history(history)
    if not insert_ok:
        raise SystemError('something went wrong when inserting data into db')