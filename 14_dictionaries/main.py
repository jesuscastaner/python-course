# dictionary = a collection of {key:value} pairs
#              ordered, mutable, duplicates allowed

capitals = {
    "Spain": "Madrid",
    "France": "Paris",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Portugal": "Lisbon",
    "United Kingdom": "London",
}

# get()
print(capitals.get("Spain"))

country = "Japan"
if capitals.get(country):
    print(f"{country} is registered")
else:
    print(f"{country} is NOT registered")

# update()
capitals.update({"Germany": "New Berlin"})
print(capitals.get("Germany"))

# pop(), popitem()
capitals.pop("France")
print(capitals.get("France"))  # None

capitals.popitem()  # removes last item
print(capitals)

# keys(), values(), items()
print("------ KEYS ------")
keys = capitals.keys()
for key in keys:
    print(key)

print("------ VALUES ------")
values = capitals.values()
for value in values:
    print(value)

print("------ ITEMS ------")
items = capitals.items()
for key, value in items:
    print(f"{key:12} {value}")
