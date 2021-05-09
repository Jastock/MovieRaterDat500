from mrjob.job import MRJob
import pandas as pd

class Pre(MRJob):
    def mapper(self, _, line):
        rating = line.split(',')
        movie_rating = {rating[1]: rating[2]}
        yield movie_rating, 1





if __name__ == '__main__':
    Pre.run()