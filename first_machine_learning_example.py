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

# Create training and test sets
# 0.2 equals to 20percent of the dataset will be held back for the test set and
# will not be put into the training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Create the regressor: reg
reg = LinearRegression()

# Fit the regressor to the training data
# How do i get a print of that if I am not in a jupiter notebook ????
reg.fit(X_train, y_train)


# predict on the test data: y_pred
y_pred = reg.predict(X_test)
print(y_pred)

# Compute and print RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse}")