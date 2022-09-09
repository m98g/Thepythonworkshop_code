import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('HTRU_2.csv')
print(df.head())
print(df)

# the data of the first star (in the column headers) will be dropped but is not
# important as its a negative one and 1 out of 17.898. Not acceptable in 
# the social sciences I recon.

df.columns = [['Mean of integrated profile', 'Standard deviation of integrated profile',
'Excess kurtosis of integrated profile', 'Skewness of integrated profile',
'Mean of MD-SNR curve', 'Standard deviation of DM-SNR curve',
'Excess kurtosis of DM-SNR curve', 'Skewness of DM-SNR curve', 'Class']]

# Dont quite get the notation in the brackets.
X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

def clf_model(model):
    clf = model
    scores = cross_val_score(clf, X, y)
    print('Scores:', scores)
    print('Mean scores', scores.mean())

clf_model(LogisticRegression())

# Logistic regression classifies every row into either 0 or 1. Scores above 0.5 = 1
# and scores below 0.5 = 0. While this takes place a decimal closer to 1 or 0 means
# that it is more likely to be correct.

### Randomforrests, KNN and Decision Trees can all be used as regressors (to get 
### continious values) or as classifiers (to get two or more end values).

clf_model(GaussianNB())
clf_model(KNeighborsClassifier())
clf_model(DecisionTreeClassifier())
clf_model(RandomForestClassifier())

# Use classifiers if the target column (y) has a finite number of possible outcomes.
# Dummys, Nominal, Categorial e.g.
# Naive Bayes is known to work well with text data.
# Random forests are known to work well generally.

print(df.Class.count())
print(df[df.Class == 1].Class.count())
print(df[df.Class == 1].Class.count() / df.Class.count())

# on this dataset it is easy to get good accuracy as 91% of rows are not 
# acturally pulsars so if the algorithm would deem every datapoint to be 0 on the
# class variable the algo would still retain a 91% accuracy.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

def confusion(model):
    clf = model
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print('Confusion Matrix:', confusion_matrix(y_test, y_pred))

    print('Classification Report:', classification_report(y_test, y_pred))
    return clf

confusion(LogisticRegression())
confusion(KNeighborsClassifier())
confusion(GaussianNB())
confusion(RandomForestClassifier())
# have to read what the heck recall actually is.

clf_model(AdaBoostClassifier())
confusion(AdaBoostClassifier())
# Adaboost is very accurate and has a good reputation.