# conditional expression = a one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          "x if condition else y"

a = 5
b = 10

# positive or negative
print("Positive" if a > 0 else "Negative")

# even or odd
result = "EVEN" if a % 2 == 0 else "ODD"
print(result)

# min and max
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Max: {max_num}")
print(f"Min: {min_num}")

# adult or child
age = 34
status = "Adult" if age >= 18 else "Child"
print(f"Status: {status}")

# hot or cold
temperature = 20
weather = "HOT" if temperature >= 20 else "COLD"
print(f"Weather: {weather}")
