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
import test_routes

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    now = dt.datetime.now()
    return f'[{now.strftime("%d/%m/%Y %H:%M:%S")}] Greenstocks Api Server up and running...'

# test routing
app.add_url_rule('/api/v1/test', view_func=test_routes.test)
app.add_url_rule('/api/v1/resources/books/all', view_func=test_routes.apitest_books_all)
app.add_url_rule('/api/v1/resources/stocks/filtered', view_func=test_routes.api_stocks_filtered)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000,debug=True)



