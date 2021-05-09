from mrjob.job import MRJob
import sklearn
from sklearn import tree
import pandas as pd
import pickle
import jsonpickle

class RF(MRJob):
    train_set = '/home/janf/PycharmProjects/MovieRater/src/train_set.csv'

    def mapper(self, _, line):
        ratings = pd.read_csv(self.train_set)
        ratings = ratings.sample(round(len(ratings.index)/10))
        tree = sklearn.tree.DecisionTreeRegressor()
        labels = ratings.iloc[:, 3]
        ratings = ratings.drop(ratings.columns[[3]], axis=1)
        samples = ratings
        tree.fit(samples, labels)
        yield jsonpickle.encode(tree), 1


if __name__ == '__main__':
    RF.run()
