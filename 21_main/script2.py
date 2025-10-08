# this is an example script
# it should run only standalone

from script1 import *


def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")


print("This is script2")
favorite_food("sushi")  # imported from script1
favorite_drink("coffee")
print('Goodbye!')
