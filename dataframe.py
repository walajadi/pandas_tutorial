import pandas as pd
import os

# read data 
# use dict to build dataframe + specify columns
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
# print(football)

# read from csv
from_csv = pd.read_csv('mariano-rivera.csv')
# from_csv.head()

# to csv
cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton.csv', sep=',', header=None,
                         names=cols)

# save dataframe to csv
# print(no_headers.head())
no_headers.to_csv('peyton_to_csv_format.csv')
os.remove('peyton_to_csv_format.csv')

# write to excel
# use football to excel : pip install xlrd, openpyxl
football.to_excel('football.xlsx', index=False)

# get clipboard
hank = pd.read_clipboard()

print(hank.head())
# store clipboard in csv
# hank.to_csv('soccer_20016_table.csv')

# Access data frame.
# use iloc
print(football.iloc[0])

# use loc for index 
print(football.loc[:2]) # get first 2 elements
print(football.loc[2:4]) # get elements from 2 to 4

# add index
print(football.index)
modified_index = football.set_index('losses')
print(modified_index.index)


