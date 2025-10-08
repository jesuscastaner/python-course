# collection = a single "variable" used to store multiple values
#              List  = []  ordered,   mutable,                        duplicates allowed
#              Set   = {}  unordered, immutable (but can add/remove), duplicates NOT allowed
#              Tuple = ()  ordered,   immutable,                      duplicates allowed

# List []
print("--------- LIST [] ---------")

fruits = ["apple", "orange", "banana", "pineapple", "coconut"]

# indexing
print(fruits)
print(fruits[0])
print(fruits[1:3])
for fruit in fruits:
    print(fruit)

# length of the list
print(f"Number of fruits: {len(fruits)}")

# check if an item exists in the list
print(f"Is there a pineapple?: {'pineapple' in fruits}")
print(f"Is there a pear?: {'pear' in fruits}")

# reassign values at i index
fruits[0] = "coconut"
print(fruits)

# append()
fruits.append("lemon")
print(fruits)

# remove()
fruits.remove("coconut")  # removes first occurence
print(fruits)

# insert()
fruits.insert(0, "lemon")
print(fruits)

# sort(), reverse()
fruits.sort()  # ascending order
print(fruits)

fruits.reverse()  # descending order
print(fruits)

# index()
print(f"There is a lemon at index {fruits.index('lemon')}")
# print(fruits.index("strawberry"))  # if not existent, an error will occur

# count()
print(f"Number of lemons: {fruits.count("lemon")}")
print(f"Number of bananas: {fruits.count("banana")}")
print(f"Number of strawberries: {fruits.count("strawberry")}")

# clear()
fruits.clear()
print(fruits)  # empty

# Set {}
print("--------- SET {} ---------")

colors = {"red", "green", "blue", "yellow"}

print(colors)  # order is not preserved
# print(colors[0])  # indexing is not possible
print(f"Number of colors: {len(colors)}")
print(f"Is there blue?: {'blue' in colors}")
print(f"Is there purple?: {'purple' in colors}")

# add(), remove()
colors.add("pink")
colors.add("pink")  # duplicates are ignored
print(colors)

colors.remove("red")
print(colors)

# Tuple ()
print("--------- TUPLE () ---------")

names = ("Jesus", "Paula", "David", "Jesus", "Laura")

print(names)
print(names[0])
print(f"Number of coordinates: {len(names)}")
print(f"Is Laura there?: {'Laura' in names}")
print(f"Is Jose there?: {'Jose' in names}")
# names[0] = "Jorge"  # tuples are immutable
print(f"David is at index {names.index('David')}")
print(f"Number of times Jesus appears: {names.count('Jesus')}")

