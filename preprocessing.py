import pandas as pd

RATINGS = '/home/janf/PycharmProjects/MovieRater/data/ratings.csv'
MOVIES = '/home/janf/PycharmProjects/MovieRater/data/movies_metadata.csv'

ratings = pd.read_csv(RATINGS)
movies = pd.read_csv(MOVIES)

ratings = ratings.drop(columns=['userId', 'timestamp'])
ratings = ratings.groupby('movieId')
meanRatings = pd.DataFrame(columns=['movieId', 'meanRating'])
for name, group in ratings:
    meanRatings = meanRatings.append({'movieId':name, 'meanRating':sum(group['rating'])/len(group['rating'])},
                                     ignore_index=True)


#movies = movies.drop(columns=['adult', 'belongs_to_collection', 'homepage', 'imdb_id', 'original_title', 'overview', 'poster_path', 'tagline', 'video', 'genres', 'production_companies', 'production_countries', 'spoken_languages'])
movies = movies.drop_duplicates(['id'])


meanRatings = meanRatings.set_index('movieId').join(movies)
#ratings = ratings.dropna()
#ratings['genres'] = ratings['genres'].replace('\[|\]|\{|\}|\'|\:|name|id|[0-9]|\,|\ ','',regex=True)
#ratings['genres'] = ratings['genres'].replace('([a-z])([A-Z])',r'\1, \2',regex=True)

#ratings['production_companies'] = ratings['production_companies'].replace('\[|\]|\{|\}|\'|\:|name|id|[0-9]|\,|\ ','',regex=True)
#ratings['production_companies'] = ratings['production_companies'].replace('([a-z])([A-Z])',r'\1, \2',regex=True)

#movies = movies['genres'].str.extract(r'')
meanRatings.to_csv('merged_data.csv')

#movies = movies.set_index('id')
#movies = movies.to_dict(orient='index')

#print(movies)
#for rating in ratings.itertuples():
#    if rating['movieI']

#print(ratings.head)
