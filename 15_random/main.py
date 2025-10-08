#

import random

number = random.random()  # returns float between 0 and 1

# roll a dice
number = random.randint(1, 6)
print(number)

# play rock, paper, scissors
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# shuffle cards
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
