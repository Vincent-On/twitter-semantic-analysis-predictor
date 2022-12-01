import pandas as pd
import warnings

# sklearn imports
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB

# Custom module imports
from data_visualization import stop_words_master

# Filter those pesky user warnings
warnings.filterwarnings('ignore')
"""
Multinomial Naive Bayes module
"""


def data_preprocessing(seed: int, data: pd.DataFrame):
    """
    Splits the data into test and training sets randomly.

    :param data: pd.DataFrame, dataset to be processed
    :param seed: int, set seed of 'random' shuffling
    :return: tuple, 4 DataFrames that contain the training features, test features, training labels, and test labels
    respectively.
    """
    # Split features/labels
    x = data[['User', 'Content']]
    y = data['Alignment']

    # Split the data between testing and training sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=seed)
    return x_train, x_test, y_train, y_test


def count_vectorizer_x_naive_bayes(n_cv: int, seed: int, data: pd.DataFrame):
    """
    Creates a classification model to score political bias and returns the best model.

    :param data: pd.DataFrame, training dataset
    :param n_cv: int, number of times you'd like to cross validate
    :param seed: int, random seed for shuffling the dataset
    :return: GridSearchCV, the model
    """
    # Dataset
    x_train, x_test, y_train, y_test = data_preprocessing(seed, data)

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
        'cvect__stop_words': [stop_words_master, 'english']
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
          f"Testing Score: {test_acc}")
    return grid_search


def evaluate_model(model: GridSearchCV, test_set: pd.DataFrame):
    users = test_set['User']
    labels = test_set['Alignment']
    prediction = model.predict(test_set['Content'])
    score = model.score(test_set['Content'], labels)
    print(f"Prediction Percentage: {score * 100}%\n")
    print(f"Prediction Preview: ")
    prediction = pd.DataFrame(prediction, columns=['Prediction'])
    output_frame = pd.concat([users, labels, prediction], axis=1)
    print(output_frame)
    return output_frame


def main():
    model = count_vectorizer_x_naive_bayes(5, 69, pd.read_csv('custom_set.csv'))
    output = evaluate_model(model, pd.read_csv('final_test_set.csv'))
    output.to_csv('output.csv')
    return


if __name__ == "__main__":
    main()
