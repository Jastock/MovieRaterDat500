from mrjob.job import MRJob
import sklearn
from sklearn import tree
import pandas as pd
import pickle
#import csv
#import numpy as np


class Train_RF(MRJob):
    train_set = 'train_set.csv'
    map_counter = 0
    red_counter = 0

    def mapper(self, _, line):
        rating = line.split(',')
        print(f"Mapper: ",  self.map_counter)
        print(rating)
        self.map_counter+= 1
        for i in range(len(rating)):
            if rating[i] == 'False':
                rating[i] = 0
            elif rating[i] == 'True':
                rating[i] = 1

        yield rating, 1

    def reducer(self, ratings, _):
        print('Reducer: ' + str(self.red_counter))
        ratings = pd.DataFrame(ratings)
        tre = tree.DecisionTreeRegressor()
        ratings = ratings.T
        label = ratings.iloc[:, 2]
        print(label)
        ratings = ratings.drop([2], axis=1)
        sample = ratings
        tre.fit(sample, label)
        filename = 'model_' + str(self.red_counter) + '.pkl'
        with open(filename, 'wb') as f:
            pickle.dump(tre, f)
        yield filename, 1



if __name__ == '__main__':
    Train_RF.run()