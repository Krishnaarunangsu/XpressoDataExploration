import  pandas as pd


s = pd.Series([90, 91, 85])
print(s)

print(s.isin([90, 92, 85]))
print(f'Percent Change:\n{s.pct_change()}')

a: float = (85-91)/91
print(a)

s = pd.Series([90, 91, None, 85])
print(s)

print(s.pct_change(fill_method='pad'))
print(s.pct_change(fill_method='ffill'))
