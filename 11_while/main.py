# while loop = keep doing something while some condition remains true

# keep asking for a non-empty input
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Try again: ")

print(f"Hello, {name}!")

# keep asking for a valid input
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Try again: "))

print(f"You are {age} years old")

# add conditional operators
# example 1
food = input("Enter a food you like (or 'q' to quit): ")

while not food == 'q':
    print(f"You like {food}")
    food = input("Enter another food you like (or 'q' to quit): ")

print("Bye!")

# example 2
num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Try again: "))

print(f"{num} is valid!")
