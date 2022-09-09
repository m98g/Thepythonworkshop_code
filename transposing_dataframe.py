import pandas as pd

test_dict = {'Corey': [63, 75, 88], 'Kevin': [48, 98, 92], 'Akshay': [87, 86, 85]}

df = pd.DataFrame(test_dict)

df = df.T # Transposing the DataFrame

df.columns = ['Quiz_1', 'Quiz_2', 'Quiz_3'] # labeling the columns in the 
# transposed DataFrame

print(df)
print(df.iloc[0])
print(df['Quiz_1'])
print(df.Quiz_1) #has its limits use the bracket notation instead
