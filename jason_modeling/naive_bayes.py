import pandas as pd

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB

from data_visualization import stop_words_master
"""
Multinomial Naive Bayes module
"""


def data_preprocessing(file_path: str, seed: int):
    """
    Splits the data into test and training sets randomly.

    :param seed: int, set seed of 'random' shuffling
    :param file_path: string, file path
    :return: tuple, 4 DataFrames that contain the training features, test features, training labels, and test labels
    respectively.
    """
    data = pd.read_csv(file_path)
    # Split features/labels
    x = data[['User', 'Content']]
    y = data['Alignment']

    # Split the data between testing and training sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=seed)
    return x_train, x_test, y_train, y_test


def count_vectorizer_x_naive_bayes(n_cv: int, seed: int, file_path: str):
    """
    Creates a classification model to score political bias and returns the best model.

    :param file_path: string, location of the dataset
    :param n_cv: int, number of times you'd like to cross validate
    :param seed: int, random seed for shuffling the dataset
    :return: GridSearchCV, the model
    """
    # Dataset
    x_train, x_test, y_train, y_test = data_preprocessing(file_path, seed=seed)

    # Pipeline Creation
    print("Generating Pipeline...")
    cvect_naive_pipeline = Pipeline([
        ('cvect', CountVectorizer()),
        ('nb', MultinomialNB())
    ])

    # Pipeline Params
    pipe_params = {
        'cvect__max_features': [None, 25, 100, 500],
        'cvect__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'cvect__stop_words': [None, stop_words_master, 'english']
    }

    # Grid search for best params
    print("Running Grid Search...")
    grid_search = GridSearchCV(cvect_naive_pipeline, param_grid=pipe_params, cv=n_cv, verbose=1, n_jobs=5)
    grid_search.fit(x_train['Content'], y_train)

    # Getting Best Stats and Parameters
    best_score = grid_search.best_score_
    best_params = grid_search.best_params_

    # Using best params to score modelling
    train_acc = grid_search.score(x_train['Content'], y_train)
    test_acc = grid_search.score(x_test['Content'], y_test)

    print(f"Highest Training Score: {best_score}\n"
          f"Params Used: {best_params}\n"
          f"Training Score: {train_acc}\n"
          f"Testing Score: {test_acc}")
    return grid_search


def main():
    count_vectorizer_x_naive_bayes(5, 69, 'custom_set.csv')
    return


if __name__ == "__main__":
    main()
