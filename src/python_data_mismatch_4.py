import sys
from io import StringIO
import pandas as pd


DF1 = StringIO("""Date       Fruit  Num  Color Country
2013-11-24 Banana 22.1 Yellow
2013-11-24 Orange  8.6 Orange
2013-11-24 Apple   7.6 Green
2013-11-24 Celery 10.2 Green
2013-11-24 Mango 15.2 Yellow
2013-11-24 Pears 15.2 Yellow India
""")
DF2 = StringIO("""Date       Fruit  Num  Color Status
2013-11-24 Banana 22.1 Yellow
2013-11-24 Orange  8.6 Orange
2013-11-24 Apple   7.6 Green
2013-11-24 Celery 10.2 Green
2013-11-25 Apple  22.1 Red
2013-11-25 Orange  8.6 Orange
2013-11-25 Apple  9.6 Orange Good


""")


df1 = pd.read_csv(DF1, sep='\s+')
df2 = pd.read_csv(DF2, sep='\s+')
#%%
dfs_dictionary = {'DF1':df1,'DF2':df2}
df=pd.concat(dfs_dictionary, sort=True)
print(df.drop_duplicates(keep=False))



# https://stackoverflow.com/questions/20225110/comparing-two-dataframes-and-getting-the-differences
# https://pythondata.com/quick-tip-comparing-two-pandas-dataframes-and-getting-the-differences/
