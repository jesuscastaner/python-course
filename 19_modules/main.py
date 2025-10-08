# module = a file (built-in or your own) containing code you want to include in your program
#          useful to break up a large program into reusable separate files
#          use 'import' to include a module
#          use 'as' to give it an alias
#          use 'from' to import only specific elements from a module
#          use '*' to import everything from a module

# import
import math

print(math.sqrt(16))

# as
import math as m

print(m.sqrt(16))

# from
from math import pi

print(pi)

# from + *
from math import *

print(factorial(5))

# from + as
from math import pi as piiii

print(piiii)

# custom module
import mymodule

x = 3
radius = 5

print("------ CUSTOM MODULE ------")
print(mymodule.pi)
print(mymodule.square(x))
print(mymodule.cube(x))
print(mymodule.circumference(radius))
print(mymodule.area(radius))
