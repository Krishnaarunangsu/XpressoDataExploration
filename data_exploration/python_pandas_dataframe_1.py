import pandas as pd
import numpy as np


df = pd.DataFrame({
                    'a': [1, 2] * 3,
                    'b': [True, False] * 3,
                    'c': [1.0, 2.0] * 3,
                    'd': ['Tom', 'John']*3
                })
print('**********************************')
print(f'Dataframe:\n{df}')
print('**********************************')
print(f'Descriptive Statistics:\n{df.describe()}')
print('**********************************')
print(f'Boolean Only:\n{df.describe(include=bool)}')
print('**********************************')
print(f'Categorical Only:\n{df.describe(include=object)}')
print('**********************************')
print(f'Exclude Numeric:\n{df.describe(exclude=[np.number])}')


df_bool = df.select_dtypes(include='bool')
print(df_bool)

df_categorical = df.select_dtypes(include='object')
print(df_categorical)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html