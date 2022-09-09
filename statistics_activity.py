import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#what the fuck does seaborn acutally do????
# makes the graphs more visually appealing and readable
sns.set()

Uk_df = pd.read_csv('UKStatistics.csv')

print(Uk_df.shape)

print(Uk_df.describe())

plt.hist(Uk_df['Actual Pay Floor (£)'])
plt.show()

x = Uk_df['Salary Cost of Reports (£)']
y = Uk_df['Actual Pay Floor (£)']

plt.scatter(x, y)
plt.show()

plt.boxplot(x)
plt.show()
plt.boxplot(y)
plt.show()