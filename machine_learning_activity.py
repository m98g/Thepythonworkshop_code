import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV


df = pd.read_csv('CHURN.csv')
print(df.head())
# the last column Chrun is my target column that I want to predict.

print(df.shape)
print(df.info())
df['Churn'] = df['Churn'].replace(to_replace=['No', 'Yes'], value=[0, 1])

X = df.iloc[:, 1:20]
y = df.iloc[:, 20]

# look up the notation for iloc as you have no idea what the first colon does.

X = pd.get_dummies(X)

def clf_model(model):
    clf = model
    scores = cross_val_score(clf, X, y)
    print('Scores:', scores)
    print('Mean score:', scores.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)

# def confusion(model):


clf_model(RandomForestClassifier())
clf_model(AdaBoostClassifier())
clf_model(KNeighborsClassifier())