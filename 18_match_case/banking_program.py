# banking program

def show_balance():
    print(f"Your balance is: {balance:,.2f} €")


def deposit():
    amount = float(input("How much do you want to deposit?: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        print(f"You deposited {amount:,.2f} €")
        return amount


def withdraw():
    amount = float(input("How much do you want to withdraw?: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    elif amount > balance:
        print("You don't have that much money")
        return 0
    else:
        print(f"You withdrew {amount:,.2f} €")
        return amount


balance = 0
is_running = True

while is_running:
    print("-----------------------------------")
    print("  1. Show balance")
    print("  2. Deposit")
    print("  3. Withdraw")
    print("  4. Exit")

    choice = input("Enter your choice (1-4): ")

    match choice:
        case "1":
            show_balance()
        case "2":
            balance += deposit()
        case "3":
            balance -= withdraw()
        case "4":
            is_running = False
        case _:
            print("Invalid choice")

print("Bye!")
