import pandas as pd

housing_df = pd.read_csv('boston_housing_1980.csv')

import matplotlib.pyplot as plt

x = housing_df['RM']
y = housing_df['MEDV']

plt.scatter(x, y)
plt.show()
