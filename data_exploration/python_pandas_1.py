import pandas as pd


dataframe_1 = pd.read_csv('../data/nba.csv')
print(f'DataFrame-NBA:\n{dataframe_1}')
print('*******************************')
print(f'DataFrame-NBA Count:\n{dataframe_1.count()}')
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html
# https://www.geeksforgeeks.org/python-pandas-dataframe-isna/
# print(f'DataFrame-NBA Count:\n{dataframe_1.count()}')
print(f'DataFrame-NBA NA Count:\n{(dataframe_1.isna()).sum()}')

dataframe_2 = pd.DataFrame()
count = 0
for (columnName, columnData) in dataframe_1.iteritems():
    print('*******************************')
    print(f'Colunm Name :{columnName}')
    print('-----------------------------------------------------')
    print(f'Unique Column Contents:\n{columnData.unique()}')
    print ('-----------------------------------------------------')
    column_na_count = columnData.isna().sum()
    print(f'NA Column Contents :\n{column_na_count}')
    if column_na_count > 0:
        if column_na_count < 10:
            count = count +1
            dataframe_2[columnName] = columnData

    print ('-----------------------------------------------------')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(count)
index_ = [item for item in range(count)]
#dataframe_2['Index'] = index_
#dataframe_2.set_index('Index')
print(dataframe_1.columns)
print(dataframe_2.columns)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(dataframe_1.head(2))
print('####################################')
print(dataframe_2.head(2))
print(dataframe_2.head(2).shape)
print('####################################')
dataframe_1['NA_COUNT_ROW'] = dataframe_1.isnull().sum(axis=1)
print(dataframe_1.head(5))
# https://cmdlinetips.com/2018/01/how-to-get-unique-values-from-a-column-in-pandas-data-frame/
# https://github.com/pandas-dev/pandas/issues/2147
# https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-49.php
# https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
# https://www.geeksforgeeks.org/create-a-new-column-in-pandas-dataframe-based-on-the-existing-columns/
# https://www.interviewqs.com/ddi_code_snippets/add_new_col_df_default_value
# https://datascience.stackexchange.com/questions/12645/how-to-count-the-number-of-missing-values-in-each-row-in-pandas-dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html
# https://www.geeksforgeeks.org/python-pandas-dataframe-count/
# https://medium.com/dunder-data/finding-the-percentage-of-missing-values-in-a-pandas-dataframe-a04fa00f84ab
# https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
# https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
# https://pynative.com/python-range-function/
# https://www.programiz.com/python-programming/methods/built-in/range
# https://thepythonguru.com/python-builtin-functions/range/
# https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
# https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
# https://thispointer.com/pandas-loop-or-iterate-over-all-or-certain-columns-of-a-dataframe/
# https://realpython.com/courses/threading-python/
# https://realpython.com/pandas-groupby/
# https://realpython.com/list-comprehension-python/
# https://realpython.com/courses/cool-new-features-python-38/
# https://www.geeksforgeeks.org/python-pandas-dataframe-select_dtypes/
# https://riptutorial.com/pandas/example/10053/selecting-columns-based-on-dtype
# https://stackoverflow.com/questions/21271581/selecting-pandas-columns-by-dtype
# https://github.com/pandas-dev/pandas/issues/16722
