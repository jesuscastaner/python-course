# math and arithmetic operations

import math

friends = 1

# sum
friends += 5
print(friends)

# rest
friends -= 2
print(friends)

# multiply
friends *= 5
print(friends)

# divide
friends /= 2  # it will output a float
print(friends)

friends = int(friends)

# power
friends **= 2
print(friends)

# modulo
friends %= 2
print(friends)

# built-in functions
# round()
x = 3.14
x = round(x)
print(f"Value of x is: {x}")

# abs()
y = -4
y = abs(y)
print(f"Value of y is: {y}")

# pow()
z = pow(y, x)
print(f"Value of z is {y}^{x} = {z}")

# max()
max_value = max(x, y, z)
print(f"Max value between x, y, z: {max_value}")

# min()
min_value = min(x, y, z)
print(f"Min value between x, y, z: {min_value}")

# some useful constants
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.15))
print(math.floor(9.15))

# calc circumference and area of a circle
radius = float(input("Enter the radius of the circle: "))
circumference = round((2 * math.pi * radius), 2)  # round decimal to 2 digits
area = round(math.pi * pow(radius, 2), 2)
print(f"The circumference of the circle is: {circumference}cm")
print(f"The area of the circle is: {area}cm^2")

# calc hypotenuse of a right triangle
a = input(float(input("Enter length of side 'a': ")))
b = input(float(input("Enter length of side 'b: ")))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Length of side 'c' is: {c}")
