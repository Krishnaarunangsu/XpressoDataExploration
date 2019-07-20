# Import Libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# This is to supress the warning messages (if any) generated in our code
import warnings
warnings.filterwarnings('ignore')

# Comment this if the data visualisations doesn't work on your side
# %matplotlib inline

# We are using whitegrid style for our seaborn plots. This is like the most basic one
sns.set_style(style = 'whitegrid')
# dataset = pd.read_csv('../input/train.csv')
dataset = pd.read_csv('train.csv')
print(dataset.info())

nrow, ncol = dataset.shape
print(nrow, ncol)


# Let's look at first few rows of our dataset
print(dataset.head(3))


# Create a separate dataframe which has only Categorical Variables
ds_cat = dataset.select_dtypes(include='object').copy()
print(ds_cat.head(2))

# Basic Stats for each variable
print(ds_cat['MSZoning'].unique())
print(len(ds_cat['MSZoning'].unique()))

# Count of distinct categories in our variable but this time we don't want to count any nan values
print(ds_cat['MSZoning'].nunique())

# Number of Missing Values in that variable (for all the rows)
print(ds_cat['MSZoning'].isnull().sum())


# Percentage of Missing Values in that variable
print(ds_cat['MSZoning'].isnull().sum()/ nrow)

# Let's multiple by 100 and keep only 1 decimal places
print((ds_cat['MSZoning'].isnull().sum()/ nrow).round(3)*100)

# Count Plot by MSZoning
sns.countplot(data = ds_cat, x = 'MSZoning')
plt.show()

# Since we are working on a supervised ML problem we should also look at the relationshipt
# between the dependent variable and independent variable. In order to do that let's add
# our dependent variable to this dataset.
ds_cat['SalePrice'] = dataset.loc[ds_cat.index, 'SalePrice'].copy()


# Basic Statistics
ds_cat_stats = pd.DataFrame(columns = ['column', 'values', 'values_Count_incna',
                                       'values_count_nona', 'num_miss', 'pct_miss'])

tmp = pd.DataFrame()
for col in ds_cat.columns:
    tmp['column'] = col
    tmp['values'] = [ds_cat[col].unique()]
    tmp['values_count_incna'] = len(list(ds_cat[col].unique()))
    tmp['values_count_nona'] = int(ds_cat[col].nunique())
    tmp['num_miss'] = ds_cat[col].isnull().sum()
    tmp['pct_miss'] = (ds_cat[col].isnull().sum() / len(ds_cat)).round(3) * 100
    ds_cat_stats = ds_cat_stats.append(tmp)

print(ds_cat_stats)

# Let's do an Ascending sort on the Number of Distinct Categories for each categorical Variables
ds_cat_stats.sort_values(by='values_count_incna', inplace=True, ascending=True)

# And set the index to Column Names
ds_cat_stats.set_index('column', inplace=True)
print(ds_cat_stats)


print(ds_cat_stats.sort_values(by='pct_miss', ascending=False).head(5))


# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-part-2
