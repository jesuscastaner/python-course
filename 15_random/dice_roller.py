# dice roller

import random
import time

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0

# ask how many dice to roll
while True:
    num_input = input("How many dice?: ")
    if num_input.isdigit() and int(num_input) > 0:
        num_of_dice = int(num_input)
        break
    print("Please enter a valid number.")

# roll each die and store their values
print("Rolling...")
time.sleep(random.random() + 1)  # waits between 1 and 2 sec

print("Results:")
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# print dice
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

# sum all values
for die in dice:
    total += die
print(f"TOTAL: {total}")
