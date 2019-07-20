import pandas as pd
import numpy as np


# create a sample of OPs unique values
series = pd.Series(
           np.random.randint(low=0, high=3, size=10))
print(series)
mapper = {0: 'New York', 1: 'London', 2: 'Zurich'}
print(mapper)
nomvar = series.replace(mapper)
print(nomvar)

# now let's use pandas.get_dummies
print(pd.get_dummies(series.replace(mapper)))


# leveraging the variables already created above
mapper = {0: 'small', 1: 'medium', 2: 'large'}
ordvar = series.replace(mapper)

print(f'Ordedred Var:{pd.factorize(ordvar)}')


preserved_mapper = {'large':2 , 'medium': 1, 'small': 0}
ordvar.replace(preserved_mapper)
print(ordvar.replace(preserved_mapper))
