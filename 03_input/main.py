# input() = a function that prompts the user to enter data
#           returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello {name}!")
print(f"You are {age} years old")

# in order to increment age value, first we need to typecast
age = int(age)
age += 1

print(f"You will be {age} next year")

# rectangle area
lenght = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = lenght * width

print(f"The area of the rectangle is {area}cm^2")

# shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is its price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Total price: {total} €")
