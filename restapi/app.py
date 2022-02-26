import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import os

from flask import Flask

import datetime as dt

# import declared  
import tests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    now = dt.datetime.now()
    return f'[{now.strftime("%d/%m/%Y %H:%M:%S")}] Greenstocks Api Server up and running...'

# test routing
app.add_url_rule('/api/v1/test', view_func=tests.test)
app.add_url_rule('/api/v1/resources/books/all', view_func=tests.apitest_books_all)
app.add_url_rule('/api/v1/resources/stocks/filtered', view_func=tests.api_stocks_filtered)
app.add_url_rule('/api/v1/resources/cryptofile', view_func=tests.api_stocks_filtered)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000,debug=True)



