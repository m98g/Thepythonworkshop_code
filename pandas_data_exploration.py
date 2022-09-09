import pandas as pd 
import numpy as np

housing_df = pd.read_csv('boston_housing_1980.csv')

## options
# print(housing_df.describe())
# print(housing_df.info())
# print(housing_df.shape)

print(housing_df.isnull().any())

print(housing_df.loc[:5, housing_df.isnull().any()])

print(housing_df.loc[:, housing_df.isnull().any()].describe())

housing_df["AGE"] = housing_df['AGE'].fillna(housing_df.mean())


housing_df['CHAS'] = housing_df['CHAS'].fillna(0)

housing_df = housing_df.fillna(housing_df.median())

print(housing_df.info())