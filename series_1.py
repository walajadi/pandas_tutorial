import pandas

# http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
import pandas as pd
import numpy as np

# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
print(s)

# specify indexes
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
	index=['A', 'Z', 'C', 'Y', 'E'])
print(s)

# create a Serie from a dict
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print(cities)

# index
print(cities['Chicago'])
print(cities[['Chicago', 'Portland', 'San Francisco']])

# boolean indexing
print(cities[cities < 1000])

# That last one might be a little weird, so let's make it more clear -
# cities < 1000 returns a Series of True/False values, which we then pass
# to our Series cities, returning the corresponding True items.

less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])

# changing values based on the index
print('changing values on index')
print('Old value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New value:', cities['Chicago'])

# changing values using boolean logic
print('changing valyes using boolean logic')
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750

print(cities[cities < 1000])

# Check values if exist
print('Check values if exist : Seattle and San Francisco')
print('Seattle' in cities)
print('San Francisco' in cities)

# divide city values by 3
print('cities divided by 3:')
print(cities / 3)

# square city values
print('square cities inhabitants')
print(np.square(cities))

# add two series
print('\n')
print('Adding two series')
print(cities[['Chicago', 'New York', 'Portland']])
print('\n')
print(cities[['Austin', 'New York']])
print('\n')
print(cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']])

# returns a boolean series indicating which values aren't NULL
cities.notnull()

# use boolean logic to grab the NULL cities
print(cities.isnull())
print('\n')
print(cities[cities.isnull()])

