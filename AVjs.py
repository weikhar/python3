# https://codereview.stackexchange.com/questions/188753/pull-stock-data-from-alpha-vantage-api

import json
import urllib.request

QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "M3CLIFYJLP54DKZA"

def _request(symbol, req_type):
    with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
        data = req.read().decode("UTF-8")
    return data

def get_daily_data(symbol):
    return json.loads(_request(symbol, 'TIME_SERIES_DAILY'))

apple = get_daily_data('AAPL')
print("Get daily price of APPLE:", apple["Time Series (Daily)"]["2018-03-02"])

