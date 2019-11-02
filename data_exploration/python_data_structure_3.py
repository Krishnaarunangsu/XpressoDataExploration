# create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()
# create a dictionary (two ways)
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)
# convert a list of tuples into a dictionary
list_of_tuples = [('dad','homer'), ('mom','marge'), ('size', 6)]
family = dict(list_of_tuples)
# examine a dictionary
family['dad'] # returns 'homer'
len(family) # returns 3
family.keys() # returns list: ['dad', 'mom', 'size']
family.values() # returns list: ['homer', 'marge', 6]
family.items() # returns list of tuples:
# [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family # returns True
'marge' in family # returns False (only checks keys)
# modify a dictionary (does not return the dictionary)