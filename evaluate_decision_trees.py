from mrjob.job import MRJob
from mrjob.compat import jobconf_from_env

import sklearn
from sklearn import tree
import pandas as pd
import pickle

class Eval_RF(MRJob):
    def mapper(self, _, line):
        yield line, 1



if __name__ == '__main__':
    Eval_RF.run()
