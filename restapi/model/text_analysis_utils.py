from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import os

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
