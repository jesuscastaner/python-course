# if = do something only if some condition is true
#      else do something else

# comparing booleans
is_online = False

if is_online:
    print("You are online")
else:
    print("You are offline")

# comparing numbers
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are NOT old enough")

# check for empty user inputs
name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name")
else:
    print(f"Hello, {name}!")
