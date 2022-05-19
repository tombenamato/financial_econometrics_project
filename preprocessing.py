import pandas as pd
import numpy as np
import re
import collections, itertools
import numpy as np
import matplotlib.pyplot as plt
import nltk
import hdbscan
import umap
import gensim

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.probability import FreqDist

from finbert_embedding.embedding import FinbertEmbedding

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.datasets import make_multilabel_classification
from sklearn.feature_extraction.text import TfidfVectorizer

from gensim import corpora
from gensim.corpora.dictionary import Dictionary

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

import glob
list_articles = glob.glob("data/earning_call/*")
texts = []
for s in list_articles:
    with open(s) as f:
        texts.append(f.read())
        
        
# Function that transforms a list of strings into 1 big concatenated string and vice-versa
def list_to_text(list_input, stops = []):
    text_output = ' '.join([word for word in list_input if word not in stops]) 
    return text_output

def text_to_list(text_input):
    list_output = word_tokenize(text_input)
    return list_output

text = 'blablabla'
# Ponctuation
text = re.sub('[^A-Za-z0-9]+', ' ', text)

# Lower all words
text = text.lower()

# Remove stopwords
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_text = [w for w in word_tokens if not w.lower() in stop_words]

# N-Gram
def ngrams_list(n):
    """
        Compute ngrams.
        
        Args:
            n (int): the number of words to words to assemble in the ngram.
        
        Returns :
            A list composed of the ngrams.
    """
    m = []
    nx_grams = ngrams(sequence = nltk.word_tokenize(text), n = n)
    for gram in nx_grams:
        m.append(gram)
    return m

wordnet_lemmatizer = WordNetLemmatizer()

# Remove most frequent and least frequent words
def remove(filtered_text, a, l, h):
    """
        Remove most and least frequent words.
        Args:
            a (list) : list on which operations should be made.
            l (float): the proportion of top l% least frequent words to remove from the numer of different words.
            h (float): the proportion of top h% most frequent words to remove from the numer of different words.
    
        Returns:
            A copy of the input text without frequent and infrequent words.
    """
    f = FreqDist(a)

    df_fdist = pd.DataFrame({'Word': f.keys(), 'Number of apparitions': f.values()})
    L= l*len(df_fdist)
    L=int(L)

    H=h*len(df_fdist)
    H=int(H)
    
    df_fdesc = df_fdist.sort_values(by='Number of apparitions', ascending=False)
    df_fasc = df_fdist.sort_values(by='Number of apparitions', ascending=True)

    most_freq_words_list = list(df_fdesc['Word'][:H])
    least_freq_word_list = list(df_fasc['Word'][:L])
    stopwords = most_freq_words_list + least_freq_word_list
    textlist_wo_extremes = list_to_text(filtered_text, stopwords)
    #text_wo_extremes = ' '.join([word for word in filtered_text if word not in stopwords]) 

    return textlist_wo_extremes

def processing(text):
    """Function that combien all the processing steps"""
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [w for w in word_tokens if not w.lower() in stop_words]
    x = [wordnet_lemmatizer.lemmatize(word, pos='n') for word in filtered_text]
    return remove(filtered_text, x,0.03,0.06)