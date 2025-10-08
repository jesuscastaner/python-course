# concession stand program
from traceback import format_tb

menu = {
    "pizza": 3.75,
    "nachos": 4.5,
    "popcorn": 5,
    "fries": 2.5,
    "chips": 1,
    "pretzel": 3.5,
    "soda": 3,
    "lemonade": 4.25,
    "water": 1.5
}

cart = []
total = 0

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:15} {value:.2f} €")
print("----------------------")

while True:
    food = input("Select and item ('q' to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food} added to cart".capitalize())
    else:
        print("That item is not on the menu.")

if len(cart) == 0:
    print("No items added to cart")
else:
    print("-------- CHECK -------")
    for food in cart:
        price = menu.get(food)
        print(f"{food:15} {price:.2f} €")
        total += price

    print("----------------------")
    print(f"{"TOTAL":15} {total:.2f} €")