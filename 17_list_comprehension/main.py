# list comprehension = a concise way to create lists
#                      [expression for value in iterable if condition]

# without condition
doubles = [x * 2 for x in range(1, 11)]
triples = [y * y for y in range(1, 11)]

print("--------------------------")
print(doubles)
print(triples)

fruits = ["apple", "banana", "orange", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print("--------------------------")
print(fruits)
print(fruit_chars)

# with condition
numbers = [1, -3, 2, -1, -5, 6, 0, 9, -1]

positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 == 1]

print("--------------------------")
print(f"{'All numbers:':17} {numbers}")
print(f"{'Positive numbers:':17} {even}")
print(f"{'Negative numbers:':17} {odd}")
print(f"{'Even numbers:':17} {even}")
print(f"{'Odd numbers:':17} {odd}")
