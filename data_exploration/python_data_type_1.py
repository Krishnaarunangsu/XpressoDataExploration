# determine the type of an object
type(2)  # returns 'int'
type(2.0)  # returns 'float'
type('two')  # returns 'str'
type(True)  # returns 'bool'
type(None)  # returns 'NoneType'
# check if an object is of a given type
isinstance(2.0, int)  # returns False
isinstance(2.0, (int, float))  # returns True
# convert an object to a given type
float(2)
int(2.9)
str(2.9)
# zero, None, and empty containers are converted to False
bool(0)
bool(None)
bool('')  # empty string
bool([])  # empty list
bool({})  # empty dictionary
# non-empty containers and non-zeros are converted to True
bool(2)
bool('two')
bool([2])
