import sklearn
from sklearn import ensemble
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
#enc = preprocessing.OneHotEncoder()
#enc.fit(label_encoded)
#onehotlabels = enc.transform(label_encoded).toarray()
'''
rf = sklearn.ensemble.RandomForestRegressor(verbose=1, n_jobs=6)
print("Fitting data")
rf.fit(train_set.drop(columns=['rating']), train_set['rating'])
print("Predicting")
predicted = rf.predict(test_set.drop(columns=['rating']))
fig, ax = plt.subplots()
ax.scatter(predicted, test_set['rating'], edgecolors=(0, 0, 1))
ax.plot([test_set['rating'].min(), test_set['rating'].max()], [test_set['rating'].min(), test_set['rating'].max()], 'r--', lw=3)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
plt.show()
print(sklearn.metrics.mean_squared_error(test_set['rating'], predicted))
'''