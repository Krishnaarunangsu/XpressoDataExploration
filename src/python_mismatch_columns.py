import pandas as pd


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
lst_1 = list()
lst_2 = list()
for col1 in df_3.columns:
    print(col1)
    lst_1.append(col1)
print(len(lst_1))
print('**************************')
for col2 in df_4.columns:
    print(col2)
    lst_2.append(col2)
print(len(lst_2))

print('Matching Columns')
print(df_3.columns.intersection(df_4.columns))

print('df_3 column difference')

# https://developers.google.com/edu/python/lists
# https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
