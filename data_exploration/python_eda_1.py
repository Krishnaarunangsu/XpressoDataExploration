import pandas as pd
import numpy as np
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

# Describing a DataFrame. By default only numeric fields are returned.
dataframe_1 = pd.DataFrame({
                    'categorical': pd.Categorical(['d', 'e', 'f']),
                    'numeric': [1, 2, 3],
                    'object': ['a', 'b', 'c']
                   })
print('********************************* Descriptive Statistics ****************************************')
# By default only numeric fields are returned.
print(dataframe_1.describe())

print('********************************* Descriptive Statistics - Numeric Property '
      '****************************************')
# Describing a column from a DataFrame by accessing it as an attribute.
print(dataframe_1.numeric.describe())

print('********************************* Descriptive Statistics - by Numpy Number property '
      '****************************************')
# Including only numeric columns in a DataFrame description.
print(dataframe_1.describe(include=[np.number]))

print('********************************* Descriptive Statistics - by Numpy Object property '
      '****************************************')
# Including only string columns in a DataFrame description.
print(dataframe_1.describe(include=[np.object]))

print('********************************* Descriptive Statistics - by Numpy Categorical property '
      '****************************************')
# Including only categorical columns from a DataFrame description.
print(dataframe_1.describe(include='category'))

print('********************************* Descriptive Statistics - Over all '
      '****************************************')
# Describing all columns of a DataFrame regardless of data type.
print(dataframe_1.describe(include='all'))

print('********************************* Descriptive Statistics - Excluding Numeric '
      '****************************************')
# Excluding numeric columns from a DataFrame description.
print(dataframe_1.describe(exclude=[np.number]))

print('********************************* Descriptive Statistics - Excluding Objects '
      '****************************************')
# Excluding object columns from a DataFrame description.
print(dataframe_1.describe(exclude=[np.object]))
