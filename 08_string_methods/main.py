# some useful string methods

name = "Jesus Castaner"
age = "29"
phone = "(+34)600-00-00-00"

# len()
print(len(name))

# find(), rfind()
print(name.find("s"))  # returns first occurence
print(name.rfind("a"))  # returns last occurence

# capitalize(), upper(), lower()
print(name.capitalize())
print(name.upper())
print(name.lower())

# isdigit()
print(name.isdigit())  # False
print(age.isdigit())  # True
print(phone.isdigit())  # False

# isalpha()
print(name.isalpha())  # (spaces are not alphabetic chars)

# count()
print(phone.count("-"))

# replace()
print(phone.replace("-", ""))
