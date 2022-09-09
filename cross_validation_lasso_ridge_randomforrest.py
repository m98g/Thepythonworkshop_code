import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV


# load data
housing_df = pd.read_csv('HousingData.csv')
print(housing_df.head())

# drop null values
housing_df = housing_df.dropna()

# declare X and y
# standart notation is to use X for the predictor culumns and y for the target column
X = housing_df.iloc[:,:-1]
y = housing_df.iloc[:, -1]

def regression_model_cv(model, k=5):
    scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=k)
    rmse = np.sqrt(-scores)
    print('Reg rmse:', rmse)
    print('Reg mean:', rmse.mean())

# the differnece in results can be partially explained by the "small" dataset
# that we use here. With bigger datasets it will not varry as much.
regression_model_cv(LinearRegression())
regression_model_cv(LinearRegression(), k=3)
regression_model_cv(LinearRegression(), k=6)
# does perfom better than regualr Linear Regression
regression_model_cv(Ridge())
# does perform worse
regression_model_cv(Lasso())

regression_model_cv(KNeighborsRegressor(n_neighbors=4))
regression_model_cv(KNeighborsRegressor(n_neighbors=7))
regression_model_cv(KNeighborsRegressor(n_neighbors=10))


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

regression_model_cv(tree.DecisionTreeRegressor())

regression_model_cv(RandomForestRegressor())
# when I enter the n_jobs=-1 into the brackets of the Regressor I get a
# long error message withouth it runs through.
regression_model_cv(RandomForestRegressor(n_estimators= 100))

param_grid = {'max_depth': [None, 10, 30, 50, 70, 100, 200, 400],
                    'min_samples_split': [2, 3, 4, 5], 
                    'min_samples_leaf': [1, 2, 3],
                    'max_features': ['auto', 'sqrt']}

reg = RandomForestRegressor()

reg_tuned = RandomizedSearchCV(reg, param_grid, cv=5, scoring='neg_mean_squared_error')

reg_tuned.fit(X, y)

p = reg_tuned.best_params_
print(f"Best n_neighbors: {p}")
score = reg_tuned.best_score_
rsm = np.sqrt(-score)
print(f"Best score: {rsm}")

regression_model_cv(RandomForestRegressor(n_estimators=500))

# Hyperparameters are a primary key to building excellent machine learning models. 
# Anyone with basic machine learning training can build machine learning models using 
# default hyperparameters. Using GridSearchCV and RandomizedSearchCV to fine-tune 
# hyperparameters to create more efficient models distinguishes advanced users from 
# beginners.