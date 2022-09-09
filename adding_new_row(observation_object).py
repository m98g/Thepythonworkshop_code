import pandas as pd
import numpy as np
# Create dictionary of test scores
test_dict = {'Corey':[63,75,88], 'Kevin':[48,98,92], 'Akshay': [87, 86, 85]}
# Create DataFrame
df = pd.DataFrame(test_dict)
df = df.T
print(df)
# Rename Columns
df.columns = ['Quiz_1', 'Quiz_2', 'Quiz_3']
print(df)

df['Quiz_4'] = [92, 95, 88]
print(df)

df_new = pd.DataFrame({'Quiz_1':[np.NaN], 'Quiz_2':[np.NaN], 'Quiz_3': [np.NaN], 
'Quiz_4':[71]}, index=['Adrian'])
# Concatenate DataFrames
df = pd.concat([df, df_new])
# Display new DataFrame
print(df)

df['Quiz_Avg'] = df.mean(axis=1, skipna=True)
print(df)

print(df.Quiz_4.astype(float))