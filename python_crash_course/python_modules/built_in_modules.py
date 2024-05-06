# Modules and imports 
# Built-in Modules - part of python but must be imported into file
# Standard Library
#import * imports every part of the module with their name, issue of name space pollution

import random as rand
import calendar
import math
from math import sin, cos, tan

num = rand.randint(1,6)
print(num)

print(calendar.isleap(2024))
print(calendar.isleap(2022))
print(calendar.weekday(1969, 7, 20))

print(math.cos(1))
print(math.pi)

print(sin(1))
print(cos(1))
print(tan(1))
