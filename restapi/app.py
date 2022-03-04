# from crypt import methods
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
app.add_url_rule('/api/v1/resources/stocks/greenscore/v1/<ticker>', view_func=model.get_green_score_v1)
app.add_url_rule('/api/v1/resources/stocks/greenscore/v2/<ticker>', view_func=model.get_green_score_v2)
app.add_url_rule('/api/v1/resources/stocks/greenscore/save', view_func=model.save_stock_green_score,methods=['PUT'])
app.add_url_rule('/api/v1/resources/stocks/greenscore/saved/list', view_func=model.get_stock_green_saved_scores)
app.add_url_rule('/api/v1/resources/stocks/financials/<ticker>', view_func=model.get_stock_financials)
app.add_url_rule('/api/v1/resources/stocks/recommendations/<ticker>', view_func=model.get_stock_recommendations)
app.add_url_rule('/api/v1/resources/stocks/history/<ticker>/<period>', view_func=model.get_stock_history)
app.add_url_rule('/api/v1/resources/stocks/sector/<sector>', view_func=model.get_stocks_by_sector)
app.add_url_rule('/api/v1/resources/stocks/sector/list', view_func=model.get_stocks_sector_list)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port =5099,debug=True)



