from flask import Flask, jsonify
from get_all_tickers import get_tickers as gt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_stocks_list():
    # tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)
    #tickers = gt.get_biggest_n_tickers(10, sectors=None)
    tickers = gt.get_tickers()[:5]
    return jsonify(tickers)

def get_stocks_sp500():
    #resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    session = requests.Session()
    session.verify = False

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
    resp = session.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies',headers=headers)

    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        cols = row.findAll('td')
        ticker = cols[0].text
        security = cols[1].text
        sector = cols[3].text
        subindustry = cols[4].text
        registered = cols[6].text
        founded = cols[8].text
        #tickers.append(ticker.replace('\n',''))
        tickers.append({
            "ticker" : ticker.replace('\n',''),
            "security" : security,
            "sector" : sector,
            "subindustry" : subindustry,
            "registered" : registered,
            "founded" : founded.replace('\n','')
        })

    dfSp500Tickers = pd.json_normalize(tickers)
    # dfSp500Tickers.to_csv(f'{DATA_DIR}\\sp500tickers.csv')
    print(dfSp500Tickers.head(30))
    return json.dump(tickers)

