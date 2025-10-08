# shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("What food do you want to buy? ('q' to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("-------------------------------")
for i in range(len(foods)):
    food = foods[i]
    price = prices[i]
    print(f"{food:<20}{price:>10.2f} €")

for price in prices:
    total += price

print("-------------------------------")
print(f"{'TOTAL':<20}{total:>10.2f} €")
