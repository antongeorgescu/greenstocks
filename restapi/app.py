import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import os

from flask import Flask, jsonify, session
from flask_session import Session

import datetime as dt

# import declared  
import tests
import model

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    now = dt.datetime.now()
    return f'[{now.strftime("%d/%m/%Y %H:%M:%S")}] Greenstocks Api Server up and running...'

# stock data routing
app.add_url_rule('/api/v1/resources/stocks/sp500/profile/<usecache>', view_func=model.get_stockprofiles_sp500)
app.add_url_rule('/api/v1/resources/stocks/sp500/list', view_func=model.get_stocklist_sp500)
app.add_url_rule('/api/v1/resources/stocks/news/<ticker>', view_func=model.get_stock_news)
app.add_url_rule('/api/v1/resources/stocks/greenscore/<ticker>', view_func=model.get_aggregated_tokens)
app.add_url_rule('/api/v1/resources/stocks/profile/<ticker>', view_func=model.get_stock_profile)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port =5099,debug=True)



