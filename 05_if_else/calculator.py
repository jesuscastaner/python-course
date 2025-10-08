# calculator

operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    result = round(result, 2)
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    result = round(result, 2)
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    result = round(result, 2)
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    result = round(result, 2)
    print(f"{num1} / {num2} = {result}")
else:
    print(f"'{operator}' is not a valid operator")
