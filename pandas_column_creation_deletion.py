import pandas as pd

test_dict = {'Corey':[63,75,88], 'Kevin':[48,98,92], 'Akshay': [87, 86, 85]}
# Create DataFrame
df = pd.DataFrame(test_dict)

# Limit DataFrame to first 2 rows
print(df[0:2])

df = df.T
df.columns = ['Quiz_1', 'Quiz_2', 'Quiz_3']

rows = ['Corey', 'Kevin']
cols = ['Quiz_1', 'Quiz_2']

df_spring = df.loc[rows, cols]
print(df_spring)
print(df.iloc[[0,1], [1,2]])

df['Quiz_Avg'] = df.mean(axis=1)
df['Quiz_4'] = [92, 95, 88]

del df['Quiz_Avg']
print(df)