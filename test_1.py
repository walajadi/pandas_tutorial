from pandas import DataFrame, read_csv
import pandas as pd
import os


# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

# export df to csv
df.to_csv('births1880.csv',index=False,header=False)

# read from csv
df = pd.read_csv('births1880.csv')
# specify header
df = pd.read_csv('births1880.csv', header=None)
print(df)
df = pd.read_csv('births1880.csv', names=['Names', 'Births'])
print(df)

os.remove('births1880.csv')
print(df.Births.dtypes)
print(df.Names.dtypes)

# sort
print(df['Births'].max())
sorted_df = df.sort_values(['Births'], ascending=False)
print(sorted_df.head(1))
