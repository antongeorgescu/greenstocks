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
from flask import request

from goose3 import Goose
import nltk
from nltk.corpus import stopwords

import warnings
# from ..model import text_analysis_utils

from .text_analysis_utils import custom_clean_text, remove_stems, stem_wordlist_porter
warnings.filterwarnings("ignore")

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from utils import StringBuilder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

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
    
def get_stock_financials(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stock_profile = []

    # show financials
    stock_profile.append(('stock_financials',json.loads(stock.financials.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_quarterly_financials',json.loads(stock.quarterly_financials.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_balance_sheet',json.loads(stock.balance_sheet.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_quarterly_balance_sheet',json.loads(stock.quarterly_balance_sheet.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_cashflow',json.loads(stock.cashflow.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_quarterly_cashflow',json.loads(stock.quarterly_cashflow.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_earnings',json.loads(stock.earnings.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_quarterly_earnings',json.loads(stock.quarterly_earnings.to_json(orient="table",index=False))['data']))
    
    return json.dumps(stock_profile)

def get_stock_recommendations(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stock_profile = []

    # show financials
    stock_profile.append(('stock_major_holders',json.loads(stock.major_holders.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_institutional_holders',json.loads(stock.institutional_holders.to_json(orient="table",index=False))['data']))
    stock_profile.append(('stock_recommendations',json.loads(stock.recommendations.to_json(orient="table",index=False))['data']))

    return json.dumps(stock_profile)

def get_stock_history(ticker,period):
    
    if period not in ['5d','1mo','3mo','6mo','1y','2y','ytd']:
        return 'Specified period parameter is incorrect.Valid values are:5d,1mo,3mo,6mo,1y,2y,ytd',400

    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stock_history = stock.history(period=period,actions=False)
    # stock_history = stock.history(start='2021-01-22', end='2021-01-31', actions=False)

    return json.dumps(json.loads(stock_history.to_json(orient="table"))['data'])

def get_green_score_v1(ticker):
    
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
        article_clean = custom_clean_text(article_clean)
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
    response.append(('Green Tokens',green_tokens))
    response.append(('Green Score',round(float(green_tokens/len(freq.items())),3)))
    response.append(('Green Focus',green_focus))
    response.append(('Green Density',green_density))
    response.append(('Relevant Tokens',[t for t in freq_items if t[1] >= 5]))
    return json.dumps(response)

def get_green_score_v2(ticker):
    
    # session = requests.Session()
    
    session = requests_cache.CachedSession('yfinance.cache')
    session.verify = False
    
    stock = yfinance.Ticker(ticker,session)

    stockInfoDocs = []

    # get stock info
    stockInfo = stock.info
    businessDescription = stockInfo['longBusinessSummary']
    stockInfoDocs.append(f'{businessDescription} ')

    # show news
    dataStockNews = stock.news
    # dataStockNews = json.loads(stock.news)
    dfStockNews = pd.json_normalize(dataStockNews)
    dfStockNews.to_csv(f'{DATA_DIR}\\stocknews_{ticker}.csv')

    g = Goose()
    for d in dataStockNews:
        stockInfoDocs.append(f'{d["title"]} ')
        response = requests.get(d['link'],verify=False)
        article = g.extract(raw_html = response.text)
        article_clean = article.cleaned_text
        article_clean = custom_clean_text(article_clean)
        stockInfoDocs.append(f'{article_clean} ')
    g.close()
    
    stockInfoDocsStemmed = []
    # run word stemmatization algorithms
    for doc in stockInfoDocs:
        intext_wordlist = doc.split(' ')
        # run the stemmatization procedure (Poter algorithm)
        outtext_wordlist = stem_wordlist_porter(intext_wordlist)
        doc = " ".join(outtext_wordlist)
        stockInfoDocsStemmed.append(doc)

    # calculate Tf-Idf with smooting
    tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,  
                                smooth_idf=True,  
                                ngram_range=(1,1),stop_words='english')
        
    tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform(stockInfoDocsStemmed)
    
    print("Calculate Tf-Idf with smoothing:")
    tf_idf_dataframe_smooth=pd.DataFrame(tf_idf_data_smooth.toarray(),columns=tf_idf_vec_smooth.get_feature_names())
    all_words = json.loads(tf_idf_dataframe_smooth.to_json(orient='table',index=False))['data'][0]

    tf_idf_dataframe = remove_stems(tf_idf_dataframe_smooth)
    print(tf_idf_dataframe)

    result = json.loads(tf_idf_dataframe.to_json(orient='table',index=False))['data'][0]
    result_sorted = sorted(result.items(), key=lambda x: x[1], reverse=True)

    green_score,green_words = text_analysis_utils.calculate_green_score_v2(result_sorted)

    return json.dumps((("green_score",green_score),("green_words",green_words),("all_words",all_words)))

def save_stock_green_score():
    ticker = request.json["ticker"]
    score_version = request.json["version"]
    score_value = request.json["score"]
    
    # read green score file
    dfgscores = pd.read_csv(f'{DATA_DIR}\green_stock_scores.csv')    
    print(dfgscores)

    # find ticker
    dfselected = dfgscores[dfgscores['ticker'] == ticker]
    if dfselected.empty:
        if score_version == 'v1':
            gscore_v1 = score_value
            gscore_v2 = '_'
        elif score_version == 'v2':
            gscore_v1 = '_'
            gscore_v2 = score_value
        dfgscores = dfselected.append({'ticker':ticker,'green_score_v1':gscore_v1,'green_score_v2':gscore_v2},ignore_index=True)   
    else:
        # get row index for ticker
        index = dfgscores.index
        condition = dfgscores["ticker"] == ticker
        ticker_rowindex = int(index[condition].tolist()[0])
        if score_version == 'v1':
            dfgscores.at[ticker_rowindex,'green_score_v1'] = score_value
        elif score_version == 'v2':
            dfgscores.at[ticker_rowindex,'green_score_v2'] = score_value
    dfgscores.to_csv(f'{DATA_DIR}\green_stock_scores.csv',index=False)
    return 200

def get_stock_green_saved_scores():
    # read green score file
    dfgscores = pd.read_csv(f'{DATA_DIR}\green_stock_scores.csv')    
    result = dfgscores.to_json(orient='table',index=False)
    return json.dumps(json.loads(result)["data"])

    
