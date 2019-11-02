# 'generic import' of math module
import math
math.sqrt(25)

# import a function
from math import sqrt
sqrt(25)  # no longer have to reference the module

# import multiple functions at once
from math import cos, floor

# import all functions in a module (generally discouraged)
# from os import *
# define an alias

import numpy as np
# show all functions in math module
content = dir(math)