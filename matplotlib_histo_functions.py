import matplotlib.pyplot as plt
#if used in a jupiter notebook .pyplot is not needed. In a script it is.
import pandas as pd
import seaborn as sns 
housing_df = pd.read_csv('boston_housing_1980.csv')

sns.set()

title = 'Median Boston Housing Prices'
plt.figure(figsize=(10,6))
plt.hist(housing_df['MEDV'])
plt.title(title, fontsize=15)
plt.xlabel('1980 Median Value in Thousands')
plt.ylabel('Count')
plt.savefig(title, dpi=300)
plt.show()

def my_hist(column, title, xlab, ylab):
    plt.figure(figsize=(10,6))
    plt.hist(column)
    plt.title(title, fontsize = 15)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.savefig(title, dpi=300)
    plt.show()

def my_hist(column, title, xlab, ylab, bins=10, alpha=0.7, color='c'):
    title = title
    plt.figure(figsize=(10,6))
    plt.hist(column, bins=bins, range=(3,9), alpha=alpha, color=color)
    plt.title(title, fontsize=15)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.savefig(title, dpi=300)
    plt.show()