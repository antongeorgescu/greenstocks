from flask import Flask, jsonify
from get_all_tickers import get_tickers as gt

def api_stocks_filtered():
    # tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)
    #tickers = gt.get_biggest_n_tickers(10, sectors=None)
    tickers = gt.get_tickers()[:5]
    return jsonify(tickers)


    
