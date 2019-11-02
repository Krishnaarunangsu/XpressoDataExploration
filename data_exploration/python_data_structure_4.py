# create an empty set
empty_set = set()
# create a set
languages = {'python', 'r', 'java'}  # create a set directly
snakes = set(['cobra', 'viper', 'python'])  # create a set from a list
# examine a set
len(languages)  # returns 3
'python' in languages  # returns True
# set operations
languages & snakes  # returns intersection: {'python'}
languages | snakes  # returns union: {'cobra', 'r', 'java', 'viper', 'python'}
languages - snakes  # returns set difference: {'r', 'java'}
snakes - languages  # returns set difference: {'cobra', 'viper'}
# modify a set (does not return the set)
languages.add('sql')  # add a new element
languages.add('r')  # try to add an existing element (ignored, no error)
languages.remove('java')  # remove an element
