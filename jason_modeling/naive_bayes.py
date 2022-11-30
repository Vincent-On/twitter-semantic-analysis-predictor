import pandas as pd

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from data_visualization import stop_words_master
"""
Multinomial Naive Bayes module
"""


def data_preprocessing():
    data = pd.read_csv("custom_set.csv")
    return


def main():
    return


if __name__ == "__main__":
    main()