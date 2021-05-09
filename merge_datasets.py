import pandas as pd

RATINGS = '/home/janf/PycharmProjects/MovieRater/data/ratingsThe .csv'
MOVIES = '/home/janf/PycharmProjects/MovieRater/data/movies_metadata.csv'

ratings = pd.read_csv(RATINGS)
movies = pd.read_csv(MOVIES)

ratings = ratings.drop(columns=['userId', 'timestamp'])
ratings = ratings.groupby('movieId')
meanRatings = pd.DataFrame(columns=['movieId', 'meanRating'])
for name, group in ratings:
    meanRatings = meanRatings.append({'movieId':name, 'meanRating':sum(group['rating'])/len(group['rating'])},
                                     ignore_index=True)
movies = movies.drop_duplicates(['id'])
meanRatings = meanRatings.set_index('movieId').join(movies)
meanRatings.to_csv('merged_data.csv')