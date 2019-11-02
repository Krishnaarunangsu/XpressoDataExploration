# create a tuple
digits = (0, 1, 'two') # create a tuple directly
digits = tuple([0, 1, 'two']) # create a tuple from a list
zero = (0,) # trailing comma is required to indicate it's a tuple
# examine a tuple
digits[2] # returns 'two'
len(digits) # returns 3
digits.count(0) # counts the number of instances of that value (1)
digits.index(1) # returns the index of the first instance of that value (1)
# elements of a tuple cannot be modified
# digits[2] = 2 # throws an error
# concatenate tuples
digits = digits + (3, 4)
# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2 # returns (3, 4, 3, 4)
# tuple unpacking
bart = ('male', 10, 'simpson') # create a tuple