from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import os
import pandas as pd

DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   

def custom_clean_text(text):
    replace_to_none = ['.','"',"\n",'(',')',',',"'",';','’','\\']
    replace_to_blank = ['--','-',"\n\n"]
    for t in replace_to_blank:
        text = text.replace(t,' ')
    for t in replace_to_none:
        text = text.replace(t,'')
    return text

def stem_wordlist_porter(word_list):
    stemmed_wordlist = []
    #create an object of class PorterStemmer
    porter = PorterStemmer()
    for word in word_list:
        stemmed_wordlist.append("{0:20}".format(porter.stem(word)))
    return stemmed_wordlist

def stem_wordlist_lancaster(word_list):
    stemmed_wordlist = []
    #create an object of class LancasterStemmer
    lancaster=LancasterStemmer()
    for word in word_list:
        stemmed_wordlist.append("{0:20}".format(lancaster.stem(word)))
    return stemmed_wordlist

def remove_stems(dftext):
    ftext = open(f'{DATA_DIR}/stems_out.txt', 'r')
    lines = ftext.readlines()
    for l in lines:
        for s in l.split(','):
            if s in dftext.columns:
                dftext.drop(s,axis = 1,inplace=True)
    return dftext

def update_stems_out(wordlistdash):
    ftext = open(f'{DATA_DIR}/stems_out.txt', 'a')
    ftext.write(wordlistdash.replace('-',','))
    ftext.close()

def calculate_green_score_v2(dictword):
    ftext = open(f'{DATA_DIR}/green_vocabulary.txt', 'r')
    lines = ftext.readlines()
    word_list = []
    for l in lines:
        for w in l.split(','):
            word_list.append(w)
    
    # remove from dataframe all columns that are not in word_list
    dict_word = []
    for t in dictword:
        if t[0] in word_list:
            dict_word.append(t)
    
    print(dict_word)

    # calculate green_score
    agg_score = 0.0
    for w in dict_word:
        agg_score += float(w[1])
    green_score = round(float(agg_score / len(dict_word)),3)

    return green_score,dict_word
