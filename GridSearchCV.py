from Thepythonworkshop.cross_validation_lasso_ridge import regression_model_cv
import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV

# load data
housing_df = pd.read_csv('HousingData.csv')
print(housing_df.head())

# drop null values
housing_df = housing_df.dropna()

# declare X and y
# standart notation is to use X for the predictor culumns and y for the target column
X = housing_df.iloc[:,:-1]
y = housing_df.iloc[:, -1]

neighbors = np.linspace(1, 20, 20)
k = neighbors.astype(int)
param_grid = {'n_neighbors': k}
knn = KNeighborsRegressor()

knn_tuned = GridSearchCV(knn, param_grid, cv=5, scoring='neg_mean_squared_error')
knn_tuned.fit(X, y)

k = knn_tuned.best_params_
print(f"Best n_neighbors: {k}")
score = knn_tuned.best_score_
rsm = np.sqrt(-score)
print(f"Best score: {rsm}")
