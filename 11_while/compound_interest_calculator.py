# compound interest calculator

principle = 0
rate = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount can't be 0 or negative")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be 0 or negative")

while True:  # alternative syntax
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be 0 or negative")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year(s): {total:.2f}€")
