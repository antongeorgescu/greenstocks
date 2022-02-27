#!/usr/bin/env python3
#import packages
import os,sys
import inspect
import uuid
import unittest
import yfinance
import requests
import json
import requests_cache
from bs4 import BeautifulSoup
import pandas as pd
from spacy.lang.en import English
import pickle
import urllib.request

from goose3 import Goose
import nltk
from nltk.corpus import stopwords

import warnings
warnings.filterwarnings("ignore")

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from utils import StringBuilder


DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   

def get_stock_news(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    # get stock info
    stockInfo = stock.info
    businessDescription = stockInfo['longBusinessSummary']

    # show news
    dataStockNews = stock.news
    # dataStockNews = json.loads(stock.news)
    dfStockNews = pd.json_normalize(dataStockNews)
    dfStockNews.to_csv(f'{self.DATA_DIR}\\stocknews_{ticker}.csv')

    stockNews = []
    for d in dataStockNews:
        stockNews.append((d['title'],d['link']))
    print(f'=== Current #news: {len(stockNews)}')
    print(stockNews)
    return json.dumps(stockNews)
    
    # show actions (dividends, splits)
    # print(stock.actions)

    # show dividends
    # print(stock.dividends)

    # show splits
    # print(stock.splits)

    # show financials
    # print(stock.financials)
    # print(stock.quarterly_financials)

    # show major holders
    # print(stock.major_holders)

    # show institutional holders
    # print(stock.institutional_holders)

    # show balance sheet
    # print(stock.balance_sheet)
    # print(stock.quarterly_balance_sheet)

    # show cashflow
    # print(stock.cashflow)
    # print(stock.quarterly_cashflow)

    # show earnings
    # print(stock.earnings)
    # print(stock.quarterly_earnings)

    # show sustainability
    # print(stock.sustainability)

    # show analysts recommendations
    # print(stock.recommendations)

    # show options expirations
    # print(stock.options)

def get_aggregated_tokens(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stockInfoAggregated = StringBuilder()

    # get stock info
    stockInfo = stock.info
    businessDescription = stockInfo['longBusinessSummary']
    stockInfoAggregated.Append(f'{businessDescription} ')

    # show news
    dataStockNews = stock.news
    # dataStockNews = json.loads(stock.news)
    dfStockNews = pd.json_normalize(dataStockNews)
    dfStockNews.to_csv(f'{self.DATA_DIR}\\stocknews_{ticker}.csv')

    g = Goose()
    for d in dataStockNews:
        stockInfoAggregated.Append(f'{d["title"]} ')
        response = requests.get(d['link'],verify=False)
        article = g.extract(raw_html = response.text)
        article_clean = article.cleaned_text
        stockInfoAggregated.Append(f'{article_clean} ')
    g.close()

    with open(f'{self.DATA_DIR}\\aggtokens_{ticker}.txt', 'w') as f:
        fcontent = stockInfoAggregated.Text().replace('\n',' ')
        f.write(fcontent)

    tokens = [t for t in fcontent.split()]
    
    clean_tokens = tokens[:]
    
    stopworden = stopwords.words('english')

    # add more stop words
    more =  ['a','the','•','-','&',' ','None','per','none','company''s','Company''s']
    for el in more:
        stopworden.append(el)
        stopworden.append(el.capitalize())
    
    for token in tokens:
        if token in stopworden:
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)

    green_tokens= 0
    green_focus = 0 # calculate as sums of occurrences of green tokens in the sum of tokens for first 10 indexes
    sum_tokens_10 = 0
    index = 0
    for key,val in freq.items():
        index = index + 1
        print (str(key) + ':' + str(val))
        if index <= 10:
            # get sum of tokens for first 10 indexes
            sum_tokens_10 = sum_tokens_10 + val
        if str(key).upper() in ['CLEAN','ENERGY','GREEN','PLANET','EMMISSIONS','NATURAL']:
            if index <= 10:
                # if g-tokens found in the first 10 indexes, get a bonus
                green_focus = green_focus + val * (10-index)
            green_tokens = green_tokens + val
    freq.plot(20,cumulative=False)

    green_focus = round(green_focus / sum_tokens_10,2)
    green_density = round(100*float(green_tokens/len(freq.items())),2)
    print('Total Tokens:',len(freq.items()),' G-Tokens:',green_tokens,' Green Focus:',green_focus,' Green Density:',green_density)

def test_list_sp500_stocks():
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
    dfSp500Tickers.to_csv(f'{DATA_DIR}\\sp500tickers.csv')
    print(dfSp500Tickers.head(10))
