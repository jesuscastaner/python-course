# number guessing game
# (guess a random number between lowest_num and highest_num)

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print("--------- NUMBER GUESSING GAME ---------")
guess = input(f"Guess a number between {lowest_num} and {highest_num} ('q' to quit): ")

while True:
    if guess.lower() == "q":
        break

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            guess = input("That guess is out of range. Try again: ")
        elif guess < answer:
            guess = input("Too low! Try again: ")
        elif guess > answer:
            guess = input("Too high! Try again: ")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            break
    else:
        guess = input("Invalid guess. Try again: ")
