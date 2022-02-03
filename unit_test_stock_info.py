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

import warnings
warnings.filterwarnings("ignore")

class TestStockInfoStats(unittest.TestCase):
    def __init__(self):
        self.DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   
        # example of creating a test dataset and splitting it into train and test sets

    def test_load_stock_data(self):
        ticker = 'ACLS'
        
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
        

    def test_scrape_weather(self):
        page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168",verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        seven_day = soup.find(id="seven-day-forecast")
        forecast_items = seven_day.find_all(class_="tombstone-container")
        tonight = forecast_items[0]
        print(tonight.prettify())   

    def test_scrape_stock_news(self):
        ticker = 'ACLS'
        stockNews = pd.read_csv(f'{self.DATA_DIR}\\stocknews_{ticker}.csv')

        page = requests.get(stockNews.iloc[0].link,verify=False)

        articleId = str(uuid.uuid1())
        file = open(f'{self.DATA_DIR}\\articles\\{ticker}_{articleId}.html',"w",encoding="utf-8")
        file.write(page.text)
        file.close()

        # article = BeautifulSoup(page.content, 'html.parser')
        # print(article.prettify())  

    def test_entity_analysis(self):
        fileId = 'ACLS_68223a2e-850a-11ec-90a0-98af655297b0' 
        file = open(f'{self.DATA_DIR}\\articles\\{fileId}.html',"r",encoding="utf-8")
        fileContent = file.read()
        file.close()
        parser = English()
        parsedEx = parser(fileContent)
 
        print("-------------- entities only ---------------")
        # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
        ents = list(parsedEx.ents)
        tags={}
        for entity in ents:
            print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
            term=' '.join(t.orth_ for t in entity)
            if ' '.join(term) not in tags:
                tags[term]=[(entity.label, entity.label_)]
            else:
                tags[term].append((entity.label, entity.label_))
        print(tags)

if __name__ == '__main__':
    # unittest.main(TestStockInfoStats().test_load_stock_data())
    # unittest.main(TestStockInfoStats().test_scrape_weather())
    # unittest.main(TestStockInfoStats().test_scrape_stock_news())
    unittest.main(TestStockInfoStats().test_entity_analysis())

