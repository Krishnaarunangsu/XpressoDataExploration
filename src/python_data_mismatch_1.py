import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
print(df)
print('*********************************')
other = pd.DataFrame({'A': [1, 3, 3, 2], 'B': ['e', 'f', 'f', 'e']})
print(other)
print('*********************************')
print('Value is in "df" but not in "other:"')
print(df.isin(other))
print('*********************************')
print('Value is in "other" but not in "df:"')
print(other.isin(df))
