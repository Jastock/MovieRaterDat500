import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

ratings = pd.read_csv('merged_data.csv')
objects = ratings.select_dtypes(include=[object])
ratings = ratings.select_dtypes(exclude=[object])
le = preprocessing.LabelEncoder()
label_encoded = objects.apply(le.fit_transform)
ratings = ratings.join(label_encoded)

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(ratings)
ratings = pd.DataFrame(imp.transform(ratings))
ratings.dropna()
ratings = ratings.reset_index()
ratings = ratings.reindex(np.random.permutation(ratings.index))
train_set = ratings.iloc[0:round(0.9*len(ratings))]
test_set = ratings.iloc[round(0.9*len(ratings)):-1]
train_set.to_csv('train_set.csv')
test_set.to_csv('test_set.csv')
