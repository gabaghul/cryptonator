from datetime import datetime
import logging
import time
import schedule
from consts import COIN_SYMBOL, CURRENCY_INDEX
from db.repository import insert_coin_history
from service.get_currency import get_currency_value

logger = logging.basicConfig(level=logging.INFO)
def job(): 
    logging.info(f'writing at: {datetime.now()}')

    res, status_code = get_currency_value(COIN_SYMBOL, CURRENCY_INDEX)
    if status_code != 200:
        raise SystemError('something went wrong when fetching coin value')

    insert_ok = insert_coin_history(res)
    if not insert_ok:
        raise SystemError('something went wrong when inserting data into db')

schedule.every().hour.at('00:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)