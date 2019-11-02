# Import Libraries
# import inline as inline
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
# dataset = pd.read_csv('../data/train.csv')
dataset = pd.read_csv('train.csv')
print(dataset.describe())
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
# plt.show()

# Since we are working on a supervised ML problem we should also look at the relationshipt
# between the dependent variable and independent variable. In order to do that let's add
# our dependent variable to this dataset.
ds_cat['SalePrice'] = dataset.loc[ds_cat.index, 'SalePrice'].copy()
len(ds_cat.columns) # 43 means 11 rows will be needed


#  Box Plot
sns.boxplot(data = ds_cat, x='MSZoning', y='SalePrice')

# Violin Plot
sns.violinplot(data = ds_cat, x='MSZoning', y='SalePrice')

# Swarm Plot
sns.swarmplot(data = ds_cat, x='MSZoning', y='SalePrice')


# Combine Violin Plot & Swarm Plot
sns.violinplot(data = ds_cat, x='MSZoning', y='SalePrice')
sns.swarmplot(data = ds_cat, x='MSZoning', y='SalePrice', color = 'k', alpha = 0.6)


fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
sns.countplot(data = ds_cat, x = 'MSZoning', ax = ax1)

ax2 = fig.add_subplot(2,1,2)
sns.boxplot(data = ds_cat, x='MSZoning', y='SalePrice' , ax = ax2)
sns.violinplot(data = ds_cat, x='MSZoning', y='SalePrice' , ax = ax2)

# Try using VIOLIN PLOT as well. This can give you a lot of details on your underlying data


# Let's stack 3 variables (6 charts) and see how it looks like
fig = plt.figure(figsize = (15,10))
ax1 = fig.add_subplot(2,3,1)
sns.countplot(data = ds_cat, x = 'MSZoning', ax=ax1)
ax2 = fig.add_subplot(2,3,2)
sns.countplot(data = ds_cat, x = 'LotShape', ax=ax2)
ax3 = fig.add_subplot(2,3,3)
sns.countplot(data = ds_cat, x = 'LotConfig', ax=ax3)

ax4 = fig.add_subplot(2,3,4)
# sns.boxplot(data = ds_cat, x = 'MSZoning', y = 'SalePrice' , ax=ax4)
sns.violinplot(data = ds_cat, x = 'MSZoning', y = 'SalePrice' , ax=ax4)
sns.swarmplot(data = ds_cat, x = 'MSZoning', y='SalePrice', color = 'k', alpha = 0.4, ax=ax4  )
ax5: object = fig.add_subplot(2,3,5)
sns.boxplot(data = ds_cat, x = 'LotShape', y = 'SalePrice', ax=ax5)
sns.violinplot(data = ds_cat, x = 'Lhttps://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way/notebookotShape', y = 'SalePrice', ax=ax5)
sns.swarmplot(data = ds_cat, x = 'LotShape', y='SalePrice', color = 'k', alpha = 0.4, ax=ax5)
ax6 = fig.add_subplot(2,3,6)
sns.boxplot(data = ds_cat, x = 'LotConfig', y = 'SalePrice', ax=ax6)
sns.violinplot(data = ds_cat, x = 'LotConfig', y = 'SalePrice', ax=ax6)
sns.swarmplot(data = ds_cat, x = 'LotConfig', y='SalePrice', color = 'k', alpha = 0.4, ax=ax6)
plt.show()

# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way
# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way/notebook
# https://towardsdatascience.com/a-starter-pack-to-exploratory-data-analysis-with-python-pandas-seaborn-and-scikit-learn-a77889485baf