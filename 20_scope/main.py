# variable scope = where a veriable is visible and accesible
#                  scope resolution order = LEGB: Local -> Enclosed -> Global -> Built-in

# local
def local1():
    x = 1  # local
    print(x)


def local2():
    x = 2  # local
    print(x)


print("Local:")
local1()
local2()


# enclosed
def enclosed1():
    y = 1  # enclosed

    def enclosed2():
        print(y)

    enclosed2()


print("Enclosed:")
enclosed1()


# global
def global1():
    print(z)


def global2():
    print(z)


z = 3  # global

print("Global:")
global1()
global2()

# built-in
from math import e


def built_in():
    print(e)


print("Built-in:")
built_in()
