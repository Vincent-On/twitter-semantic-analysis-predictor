# Twitter Sentiment Analysis Predictor

## Introduction
This readme provides an overview of the program.

All functions and classes are documented. You can check them for params and returns.

## How to Use
1. Run `main()` in `create_dataset.py`
2. Run `main()` in `naive_bayes.py`

`naive_bayes.py` will output a csv file that contains the true and predicted alignments of
the test set.

## Module Overview
### `create_dataset.py`
This creates the dataset you will be working with.

`left` and `right` contain the twitter handles of the training data for left
wing and right wing Twitter users respectively. If you wish to add users you can add their
Twitter handle without the '@' symbol.

`left_test` and `right_test` contain the handles for the unseen data. Again, you
will have to add the user to the appropriate column so that the predictor has something 
to compare to.

`create_aligned_dataset` creates a single-alignment dataset. That is it all the users 
inputted will be of the same alignment.

It's a little clunky but main automatically merges the two into a data set for training. The
separation is intentional as it allowed for easier data visualization when the data is 
separated by alignment

### `data_visualization.py`
This module handles data visualization which is a key part of this project as it allows us
to easily identify words that should be added to the `stop_word_master` list.

When run it simply outputs two pyplot charts showing the words that appear the most often
in each political camps tweets.

### `tweeter_collection.py`
This module is a simple class that can store collections of tweets and return them
as a list of tweets or tokenized words.

### `naive_bayes.py`
Something of a misnomer as this has all the key code implementation.

`data_preprocessing()` simply takes a `DataFrame` and splits it into features, labels,
training and test sets.

`count_vectorizer_x_naive_bayes()` is where the magic happens. It takes a `DataFrame`
containing `Users`, `Content`(tweets), and `Alignment` columns.

The way it works is as follows:
1. Data is preprocessed
2. `Pipeline` is created containing the `CountVectorizer()` and `MultinomialMB()`
3. Pipeline parameters are hard coded but contain different parameters for `CountVectorizer`
4. A `GridSearchCV` object is created that runs `.fit()` operations on the training data for
every permutation of `pipe_params` and performs 5-fold cross validation on each permutation.
5. It prints the highest accuracy score it was able to achieve and the parameters used to achieve it
6. Finally, it returns the model to be used in `.predict()` later.

`evaluate_model` takes the model generated from `count_vectorizer_x_naive_bayes()` and an unseen dataset
and evaluates the performance of the model on unseen test data.
