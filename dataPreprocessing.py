import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from numpy import array
from numpy import asarray
from numpy import zeros

from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer

"""
Data Preprocess to be imported by Neural Networks
"""

tweets_data = pd.read_csv("./dataset.csv")

# TAG_RE = re.compile(r'<[^>]+>')
#
#
# def remove_tags(text):
#     return TAG_RE.sub('', text)
#
#
# def preprocess_text(sen):
#     # Removing html tags
#     sentence = remove_tags(sen)
#
#     # Remove punctuations and numbers
#     sentence = re.sub('[^a-zA-Z]', ' ', sentence)
#
#     # Single character removal
#     sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
#
#     # Removing multiple spaces
#     sentence = re.sub(r'\s+', ' ', sentence)
#
#     return sentence
#
#
# X = []
# sentences = list(tweets_data[''])
# for sen in sentences:
#     X.append(preprocess_text(sen))
#
# y = tweets_data['']
#
# y = np.array(list(map(lambda x: 1 if x == "positive" else 0, y)))
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# tokenizer = Tokenizer(num_words=5000)
# tokenizer.fit_on_texts(X_train)
#
# X_train = tokenizer.texts_to_sequences(X_train)
# X_test = tokenizer.texts_to_sequences(X_test)

# vocab_size = len(tokenizer.word_index) + 1
#
# maxlen = 100
#
# X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
# X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

# embeddings_dictionary = dict()
# glove_file = open('E:/Datasets/Word Embeddings/glove.6B.100d.txt', encoding="utf8")
#
# for line in glove_file:
#     records = line.split()
#     word = records[0]
#     vector_dimensions = asarray(records[1:], dtype='float32')
#     embeddings_dictionary [word] = vector_dimensions
# glove_file.close()

# embedding_matrix = zeros((vocab_size, 100))
# for word, index in tokenizer.word_index.items():
#     embedding_vector = embedding_dictionary.get(word)
#     if embedding_vector is not None:
#         embedding_matrix[index] = embedding_vector
