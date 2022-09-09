import pandas as pd
import matplotlib.pyplot as plt

housing_df = pd.read_csv('HousingData.csv')
import seaborn as sns

sns.set()

x = housing_df['RM']
y = housing_df['MEDV']
plt.boxplot(x)
plt.show()

plt.violinplot(x)
plt.show()