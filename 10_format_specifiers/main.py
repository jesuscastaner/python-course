# format specifiers = format a value based on what flags are inserted
#                     .<number>f, :<number>, :0<number>, :<, :>, :^, :+, ": ", ":,"

price1 = 3000.14159
price2 = -1987.6563812
price3 = 12

# .<number>f
print(".<number>f")
print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")

# :<number>
print(":<number>")
print(f"Price 1 is {price1:15}")
print(f"Price 2 is {price2:15}")
print(f"Price 3 is {price3:15}")

# :0<number>
print(":0<number>")
print(f"Price 1 is {price1:015}")
print(f"Price 2 is {price2:015}")
print(f"Price 3 is {price3:015}")

# :<
print(":<")
print(f"Price 1 is {price1:<15}")
print(f"Price 2 is {price2:<15}")
print(f"Price 3 is {price3:<15}")

# :>
print(":>")
print(f"Price 1 is {price1:>15}")
print(f"Price 2 is {price2:>15}")
print(f"Price 3 is {price3:>15}")

# :^
print(":^")
print(f"Price 1 is {price1:^15}")
print(f"Price 2 is {price2:^15}")
print(f"Price 3 is {price3:^15}")

# :+
print(":+")
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

# :
print('": "')
print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")

# :,
print(":,")
print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

# combined
print(f"Price 1 is {price1:+15,.2f} €")
print(f"Price 2 is {price2:+15,.2f} €")
print(f"Price 3 is {price3:+15,.2f} €")
