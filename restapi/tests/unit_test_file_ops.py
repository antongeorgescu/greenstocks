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
from cryptography.fernet import Fernet

import warnings
warnings.filterwarnings("ignore")

class TestFileOps(unittest.TestCase):
    def __init__(self):
        self.DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   

    def generate_encryption_key(self):
        # key generation
        key = Fernet.generate_key()
        
        # string the key in a file
        with open(f'{self.DATA_DIR}\\filekey.key', 'wb') as filekey:
            filekey.write(key)
    
    def encrypt_file(self,filepath):
        # opening the key
        with open(f'{self.DATA_DIR}\\filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        # using the generated key
        fernet = Fernet(key)
        
        # opening the original file to encrypt
        with open(filepath, 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and 
        # writing the encrypted data
        with open(filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt_file(self,filepath):
        # opening the key
        with open(f'{self.DATA_DIR}\\filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        # using the key
        fernet = Fernet(key)
        
        # opening the encrypted file
        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        with open(filepath, 'wb') as dec_file:
            dec_file.write(decrypted)
    
        
        
if __name__ == '__main__':
    # unittest.main(TestStockInfoStats().test_load_stock_data())
    # unittest.main(TestStockInfoStats().test_scrape_weather())
    # unittest.main(TestStockInfoStats().test_scrape_stock_news())
    # unittest.main(TestStockInfoStats().test_entity_analysis())
    unittest.main(TestStockInfoStats().test_list_sp500_stocks())

