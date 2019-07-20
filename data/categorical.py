import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({'quality': [1, 2, 3], 'city': [3, 2, 1]}, columns=['quality', 'city'])
print(df.describe())
print(df.info())
enc = OneHotEncoder(categorical_features=[False, True])
X = df.values
enc.fit(X)
print(enc.transform(X).todense())

