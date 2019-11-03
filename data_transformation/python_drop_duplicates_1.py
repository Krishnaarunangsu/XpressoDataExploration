import numpy as np
import pandas as pd

name: list = ['Willard Morris']
print(name)

name.extend(['Al Jennings'])
print(name)

name.extend(['Spencer MacDaniel'])
print(name)

name.insert(2, 'Omar Mullins')
print(name)


# Python program to demonstrate the
# use of join function to join list
# elements without any separator.

# Joining with empty separator
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))

# https://www.programiz.com/python-programming/methods/list/append##targetText=Python%20List%20append(),it%20modifies%20the%20original%20list.

age: tuple = (20, 19, 21, 22,)
print(type(age))

favourite_color: list = ['blue', 'blue', 'yellow', 'green']

grade: list = [88, 92, 95, 70]

raw_data: dict = {
                   'name': name,
                   'age': age,
                   'grade': grade,
                   'favourite_color': favourite_color
                  }

print(raw_data)

df = pd.DataFrame(raw_data, index=name)
print(df)

df = df.drop_duplicates(subset='favourite_color', keep="first")
print(df)

# https://www.interviewqs.com/ddi_code_snippets/drop_duplicate_rows_pandas
# https://stackoverflow.com/questions/12497402/python-pandas-remove-duplicates-by-columns-a-keeping-the-row-with-the-highest
# https://www.programiz.com/python-programming/methods/list/extend
# https://www.geeksforgeeks.org/join-function-python/