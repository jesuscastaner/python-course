# type casting = the process of converting a variable from one data type to another
#                str(), int(), float(), bool()

name = "Jesus"
age = 29
height = 1.71
is_online = True

# print types
print(type(name))
print(type(age))
print(type(height))
print(type(is_online))

# int -> float
age = float(age)

print(age)

# float -> str
age = str(age)

print(age)
print(type(age))
# age += 1  # this would get a type error because "age" is now a string, not a number

# str -> bool
name = bool(name)

print(name)  # if not empty, prints True

name = ""
print(name)  # else if empty, prints False
