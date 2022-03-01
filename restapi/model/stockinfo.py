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
    dfStockNews.to_csv(f'{DATA_DIR}\\stocknews_{ticker}.csv')

    stockNews = []
    for d in dataStockNews:
        stockNews.append((d['title'],d['link']))
    print(f'=== Current #news: {len(stockNews)}')
    print(stockNews)
    return json.dumps(stockNews)
    
def get_stock_profile(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stock_profile = []
    
    # show actions (dividends, splits)
    # print(stock.actions)

    # show dividends
    # print(stock.dividends)

    # show splits
    # print(stock.splits)

    # show financials
    stock_profile.append(('stock_financials',stock.financials))
    stock_profile.append(('stock_quarterly_financials',stock.quarterly_financials))
    stock_profile.append(('stock_major_holders',stock.major_holders))
    stock_profile.append(('stock_institutional_holders',stock.institutional_holders))
    stock_profile.append(('stock_balance_sheet',stock.balance_sheet))
    stock_profile.append(('stock_quarterly_balance_sheet',stock.quarterly_balance_sheet))
    stock_profile.append(('stock_cashflow',stock.cashflow))
    stock_profile.append(('stock_quarterly_cashflow',stock.quarterly_cashflow))
    stock_profile.append(('stock_earnings',stock.earnings))
    stock_profile.append(('stock_quarterly_earnings',stock.quarterly_earnings))
    stock_profile.append(('stock_sustainability',stock.sustainability))
    stock_profile.append(('stock_recommendations',stock.recommendations))

    return json.dumps(stock_profile)

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
    dfStockNews.to_csv(f'{DATA_DIR}\\stocknews_{ticker}.csv')

    g = Goose()
    for d in dataStockNews:
        stockInfoAggregated.Append(f'{d["title"]} ')
        response = requests.get(d['link'],verify=False)
        article = g.extract(raw_html = response.text)
        article_clean = article.cleaned_text
        stockInfoAggregated.Append(f'{article_clean} ')
    g.close()

    with open(f'{DATA_DIR}\\aggtokens_{ticker}.txt', 'w') as f:
        fcontent = stockInfoAggregated.Text().replace('\n',' ')
        f.write(fcontent)

    tokens = [t for t in fcontent.split()]
    
    clean_tokens = tokens[:]
    
    stopworden = stopwords.words('english')

    # add more stop words
    more =  ['a','the','•','-','&',' ','None','per','none','company''s','Company''s','stock','Stock']
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
    freq_items = []
    for key,val in freq.items():
        index = index + 1
        # print (str(key) + ':' + str(val))
        freq_items.append((key,val))
        if index <= 10:
            # get sum of tokens for first 10 indexes
            sum_tokens_10 = sum_tokens_10 + val
        if str(key).upper() in ['CLEAN','ENERGY','GREEN','PLANET','EMMISSIONS','NATURAL']:
            if index <= 10:
                # if g-tokens found in the first 10 indexes, get a bonus
                green_focus = green_focus + val * (10-index)
            green_tokens = green_tokens + val
    # freq.plot(20,cumulative=False,show=False)
    
    green_focus = round(green_focus / sum_tokens_10,2)
    green_density = round(100*float(green_tokens/len(freq.items())),2)
    print('Total Tokens:',len(freq.items()),' G-Tokens:',green_tokens,' Green Focus:',green_focus,' Green Density:',green_density)
    response = []
    response.append(('Total Tokens',len(freq.items())))
    response.append(('G-Tokens',green_tokens))
    response.append(('Green Focus',green_focus))
    response.append(('Green Density',green_density))
    response.append(('Relevant Tokens',[t for t in freq_items if t[1] >= 5]))
    return json.dumps(response)


