from mrjob.job import MRJob
import sklearn
from sklearn import tree
import pandas as pd
import pickle
import jsonpickle
import numpy as np

class RF_eval(MRJob):
    test_set = '/home/janf/PycharmProjects/MovieRater/src/test_set.csv'
    pred_mean = []

    def mapper(self, _, line):
        line = line[1:-3]
        line = line.replace('\\', '')
        tree = jsonpickle.decode(line)
        ratings = pd.read_csv(self.test_set)
        labels = ratings.iloc[:, 3]
        ratings = ratings.drop(ratings.columns[[3]], axis=1)
        samples = ratings
        predictions = tree.predict(ratings)

        yield (list(ratings.iloc[:, 0]), (list(predictions), list(labels)))

    def reducer(self, movies, ratings):
        movies = list(movies)
        ratings = list(ratings)
        mean_predictions = []
        for i in range(len(movies)):
            mean_rating = 0
            for j in range(len(ratings)):
                mean_rating += ratings[j][0][i]
            mean_predictions.append(mean_rating/len(ratings))
        labels = ratings[0][1]
        mea = sklearn.metrics.mean_absolute_error(labels, mean_predictions)
        mse = sklearn.metrics.mean_squared_error(labels, mean_predictions)
        r2 = sklearn.metrics.r2_score(labels, mean_predictions)
        yield movies, (mean_predictions, labels)
        yield "Mean absolute error", mea
        yield "Mean squared error", mse
        yield "R2 score", r2




if __name__ == '__main__':
    RF_eval.run()
