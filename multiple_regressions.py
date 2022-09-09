import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# load data
housing_df = pd.read_csv('HousingData.csv')
print(housing_df.head())

# drop null values
housing_df = housing_df.dropna()

# declare X and y
# standart notation is to use X for the predictor culumns and y for the target column
X = housing_df.iloc[:,:-1]
y = housing_df.iloc[:, -1]


def regression_model(model):
    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    # Create the regressor: reg_all 
    reg_all = model
    # Fit the regressor to the training data
    reg_all.fit(X_train, y_train)
    # Predict on the test data: y_pred
    y_pred = reg_all.predict(X_test)
    # Compute and print RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    #f-strings are way nicer
    print("Root Mean Squared Error: {}".format(rmse))

#scores different each time because the train and test sets are created each time 
#anew and that leads to the inconcistency. Need a way to get the same data
#to each regression
regression_model(LinearRegression())
regression_model(LinearRegression())
regression_model(LinearRegression())
regression_model(LinearRegression())
regression_model(LinearRegression())
regression_model(LinearRegression())
