import pandas as pd
import statsmodels.api as sm
housing_df = pd.read_csv('HousingData.csv')

import matplotlib.pyplot as plt

print(housing_df.corr())

import seaborn as sns
# Set up seaborn dark grid
# Heatmap to easily identify high correlations.
sns.set()
corr = housing_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap="Blues", linewidths=1.25, alpha=0.8)
plt.show()



x = housing_df['RM']
y = housing_df['MEDV']
plt.scatter(x, y) 
plt.show()
#the shadow is the 95% confidence interval
plt.figure(figsize=(10, 7))
sns.regplot(x,y)
plt.show()



X = sm.add_constant(x)
model = sm.OLS(y, x)
est = model.fit()
print(est.summary())