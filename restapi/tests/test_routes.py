from flask import Flask, jsonify
from get_all_tickers import get_tickers as gt

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

def test():
    return 'it works!'

# A function to return all of the available entries in our catalog.
def apitest_books_all():
    return jsonify(books)

def api_stocks_filtered():
    # tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)
    #tickers = gt.get_biggest_n_tickers(10, sectors=None)
    tickers = gt.get_tickers()[:5]
    return jsonify(tickers)


    
