# create an empty list (two ways)
empty_list = []
empty_list = list()
# create a list
simpsons = ['homer', 'marge', 'bart']
# examine a list
simpsons[0] # print element 0 ('homer')
len(simpsons) # returns the length (3)
# modify a list (does not return the list)
simpsons.append('lisa') # append element to end
simpsons.extend(['itchy', 'scratchy']) # append multiple elements to end
simpsons.insert(0, 'maggie') # insert element at index 0 (shifts everything␣˓→right)
simpsons.remove('bart') # searches for first instance and removes it
simpsons.pop(0) # removes element 0 and returns it
del simpsons[0] # removes element 0 (does not return it)
simpsons[0] = 'krusty' # replace element 0
# concatenate lists (slower than 'extend' method)
neighbors = simpsons + ['ned','rod','todd']
# find elements in a list
simpsons.count('lisa') # counts the number of instances
simpsons.index('itchy') # returns index of first instance
# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0] # element 0
weekdays[0:3] # elements 0, 1, 2
weekdays[:3] # elements 0, 1, 2
weekdays[3:] # elements 3, 4
weekdays[-1] # last element (element 4)
weekdays[::2] # every 2nd element (0, 2, 4)
weekdays[::-1] # backwards (4, 3, 2, 1, 0)
# alternative method for returning the list backwards
list(reversed(weekdays))
# sort a list in place (modifies but does not return the list)
simpsons.sort()
simpsons.sort(reverse=True) # sort in reverse
simpsons.sort(key=len) # sort by a key
# return a sorted list (but does not modify the original list)
sorted(simpsons)
sorted(simpsons, reverse=True)
sorted(simpsons, key=len)
# create a second reference to the same list
num = [1, 2, 3]
same_num = num
same_num[0] = 0 # modifies both 'num' and 'same_num'
# copy a list (three ways)
new_num = num.copy()
new_num = num[:]
new_num = list(num)
# examine objects
id(num) == id(same_num) # returns True
id(num) == id(new_num) # returns False
num is same_num # returns True
num is new_num # returns False
num == same_num # returns True
num == new_num # returns True (their contents are equivalent)
# conatenate +, replicate *
[1, 2, 3] + [4, 5, 6]
["a"] * 2 + ["b"] * 3