import pandas as pd

df_1 =  pd.read_csv('test1.csv')
df_2 =  pd.read_csv('test2.csv')
print(df_1)
print('*************')
print(df_2)
print('*************')


print(df_2[ ~df_2.isin(df_1)].dropna())
print('*************')


df_3 = pd.DataFrame({
'A' : [1.0, 2.0, 3.0, 4.0],
'B' : [100, 200, 300, 400],
'C' : [2, 3, 4, 5]
                   })
print('*************')
print(df_3)

df_4 = pd.DataFrame({
'B' : [1.0, 2.0, 3.0, 4.0],
'C' : [100, 200, 300, 400],
'D' : [2, 3, 4, 5]
                  })

print(df_4)
print('*************')

print(df_4.columns.difference(df_3.columns))

print('*************')

# https://stackoverflow.com/questions/43028969/pandas-return-columns-in-dataframe-that-are-not-in-other-dataframe?rq=1

df1 = pd.DataFrame({'c1': [1, 4, 7], 'c2': [2, 5, 1], 'c3': [3, 1, 1]})
df2 = pd.DataFrame({'c4': [1, 4, 7], 'c2': [3, 5, 2], 'c3': [3, 7, 5]})

print(set(df1.columns).intersection(set(df2.columns)))

print('***************************')
print(df1.where(df1.values==df2.values).notna())

print(set(df1['c2']).intersection(set(df2['c2'])))

print(df1.columns)

# https://stackoverflow.com/questions/53402012/use-column-combinations-to-find-data-mismatch-in-rows-pandas
# https://towardsdatascience.com/10-python-pandas-tricks-that-make-your-work-more-efficient-2e8e483808ba
# http://raju.shoutwiki.com/wiki/Manipulating_dataframes_in_python
# https://gist.github.com/fomightez/ef57387b5d23106fabd4e02dab6819b4
# http://raju.shoutwiki.com/wiki/Manipulating_dataframes_in_python
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
