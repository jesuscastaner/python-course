# rock, paper, scissors game

import random

options = ["rock", "paper", "scissors"]

while True:
    print("--------- ROCK, PAPER, SCISSORS ---------")

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"  - Player: {player}")
    print(f"  - Computer: {computer}")

    if player == computer:
        print("It's a tie! -_-")
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        print("You win! ^_^")
    else:
        print("You lose! u_u")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        break

print("Bye!")
