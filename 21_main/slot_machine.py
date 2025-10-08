# slot machine

import random


def spin_row(symbols):
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")


def get_payout(symbols, row, bet):
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        if symbol == symbols[0]:
            return bet * 3
        elif symbol == symbols[1]:
            return bet * 8
        elif symbol == symbols[2]:
            return bet * 20
    return 0


def main():
    symbols = ["🍒", "🍉", "⭐"]
    balance = 100

    print("--------- SLOT MACHINE ---------")

    while balance > 0:
        print(f"Current balance: {balance:,.2f} €")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough money")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row(symbols)
        print_row(row)

        payout = get_payout(symbols, row, bet)
        if payout > 0:
            print(f"You won {payout:,.2f} €")
        else:
            print("You lost this round")

        balance += payout

        play_again = input("Spin again? (y/n): ").lower()
        if play_again != "y":
            break


if __name__ == '__main__':
    main()
