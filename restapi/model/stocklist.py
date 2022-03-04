from flask import Flask, jsonify
from get_all_tickers import get_tickers as gt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os,json

DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   

def get_stockprofiles_sp500(usecache = 'True'):

    is_cache_file = os.path.isfile(f'{DATA_DIR}\\stockinfo_sp500.csv')
    use_cache = eval(usecache)
    if (not use_cache) or (use_cache and not is_cache_file):
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
        dfSp500Tickers.to_csv(f'{DATA_DIR}\\stockinfo_sp500.csv',index=False)
        # dfSp500Tickers.to_csv(f'{DATA_DIR}\\sp500tickers.csv')
        print(dfSp500Tickers.head(30))
        result = dfSp500Tickers.to_json(orient='table',index=False)
        return json.dumps(json.loads(result)['data'])
    else:
        if is_cache_file:
            # file exists, read it
            dfSp500Tickers = pd.read_csv(f'{DATA_DIR}\\stockinfo_sp500.csv')
            # dfSp500Tickers.to_csv(f'{DATA_DIR}\\sp500tickers.csv')
            print(dfSp500Tickers.head(30))
            result = dfSp500Tickers.to_json(orient='table',index=False)
            return json.dumps(json.loads(result)['data'])
    
def get_stocklist_sp500():

    is_cache_file = os.path.isfile(f'{DATA_DIR}\\stockinfo_sp500.csv')
    if not is_cache_file:
        dfallstocks = pd.read_json(get_stockprofiles_sp500(False))
    else:
        dfallstocks = pd.read_csv(f'{DATA_DIR}\\stockinfo_sp500.csv')
    
    # extract list of sector and subindustry
    lst_sectors = dfallstocks[['sector','subindustry']]
    lst_sectors.drop_duplicates(inplace=True,ignore_index=True)
    
    print(lst_sectors.head(30))
    result = lst_sectors.to_json(orient='table',index=False)
    return json.dumps(json.loads(result)['data'])

def get_stocks_by_sector(sector):

    is_cache_file = os.path.isfile(f'{DATA_DIR}\\stockinfo_sp500.csv')
    if not is_cache_file:
        dfallstocks = pd.read_json(get_stockprofiles_sp500(False))
    else:
        dfallstocks = pd.read_csv(f'{DATA_DIR}\\stockinfo_sp500.csv')
    
    # extract list of stocks per sector
    dfsector = dfallstocks[dfallstocks["sector"] == sector]
    lst_stocks = dfsector[['ticker','subindustry']]
    lst_stocks.drop_duplicates(inplace=True,ignore_index=True)
    
    print(lst_stocks.head(30))
    result = lst_stocks.to_json(orient='table',index=False)
    return json.dumps(json.loads(result)['data'])

def get_stocks_sector_list():
    is_cache_file = os.path.isfile(f'{DATA_DIR}\\stockinfo_sp500.csv')
    if not is_cache_file:
        dfallstocks = pd.read_json(get_stockprofiles_sp500(False))
    else:
        dfallstocks = pd.read_csv(f'{DATA_DIR}\\stockinfo_sp500.csv')
    
    # extract list of stocks per sector
    dfsectorlist = dfallstocks[["sector"]]
    dfsectorlist.drop_duplicates(inplace=True,ignore_index=True)
    
    result = dfsectorlist.to_json(orient='table',index=False)
    return json.dumps(json.loads(result)['data'])
