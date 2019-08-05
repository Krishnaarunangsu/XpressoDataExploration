import pandas as pd
import numpy as np


series_1 = pd.Series([20, 25, 30], index= ['London', 'New York', 'Helsinki'])
print(f'Temperature:\n{series_1}')
print('********************************************')

# Square the values by defining a function and
# passing it as an argument to apply().
def square(x):
    """
    Squares a numeric value
    Args:
        x: numeric
    Returns:
        Square of x
    """
    return x**2

series_2 = series_1.apply(square)
print(f'Temperature squared:\n{series_2}')
print('********************************************')

# Square the values by passing an anonymous function as an argument to apply().
series_3 = series_1.apply(lambda x: x**2)
print(f'Temperature squared:\n{series_3}')
print('********************************************')


# Define a custom function that needs additional positional arguments and
# pass these additional arguments using the args keyword.
def subtract_custom_value(x, custom_value):
    """
    Subtraction from x
    Args:
        x: Numeric from which subtraction will take place
        custom_value: value to be subtracted from x

    Returns:
        subtraction result

    """
    return (x - custom_value)

series_4 = series_1.apply(subtract_custom_value, args=(5,))
print(f'Temperature After subtraction:\n{series_4}')
print('********************************************')



# Define a custom function that takes keyword arguments and pass these arguments to apply.
def add_custom_values(x,**kwargs):
    """
    Args:
        **kwargs:argument list

    Returns:
        Added values

    """
    for month in kwargs:
        x+= kwargs[month]
        return x

# Define a custom function that takes keyword arguments and pass these arguments to apply.
series_5 = series_1.apply(add_custom_values, june = 20, july = 25, august = 30)
print(f'Temperature After Addition:\n{series_5}')
print('********************************************')

# Use a function from the Numpy library
series_6 = series_1.apply(np.log)
print(f'Logarthimic Values of Temperature:\n{series_6}')


# https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.apply.html
