import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os
import unittest

class TestTextAnalysis(unittest.TestCase):
    def __init__(self):
        self.DATA_DIR = f'{os.path.dirname(os.path.abspath(__file__))}\\data'   
        # example of creating a test dataset and splitting it into train and test sets

    def test_extraction_tf_idf_vectorizer(self):
        sentence_1="This is a good job.I will not miss it for anything"
        sentence_2="This is not good at all"
        
        #without smooth IDF
        print("Without Smoothing:")
        #define tf-idf
        tf_idf_vec = TfidfVectorizer(use_idf=True, 
                                smooth_idf=False,  
                                ngram_range=(1,1),stop_words='english') # to use only  bigrams ngram_range=(2,2)
        #transform
        tf_idf_data = tf_idf_vec.fit_transform([sentence_1,sentence_2])
        
        #create dataframe
        tf_idf_dataframe=pd.DataFrame(tf_idf_data.toarray(),columns=tf_idf_vec.get_feature_names())
        print(tf_idf_dataframe)
        print("\n")
        
        #with smooth
        tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,  
                                smooth_idf=True,  
                                ngram_range=(1,1),stop_words='english')
        
        tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform([sentence_1,sentence_2])
        
        print("With Smoothing:")
        tf_idf_dataframe_smooth=pd.DataFrame(tf_idf_data_smooth.toarray(),columns=tf_idf_vec_smooth.get_feature_names())
        print(tf_idf_dataframe_smooth)

    def test_sort_dictionary(self):
        orders = {
            'cappuccino': 54,
            'latte': 56,
            'espresso': 72,
            'americano': 48,
            'cortado': 41
        }

        sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

        for i in sort_orders:
            print(i[0], i[1])

if __name__ == '__main__':
    # unittest.main(TestTextAnalysis().test_extraction_tf_idf_vectorizer())
    unittest.main(TestTextAnalysis().test_sort_dictionary())
    
