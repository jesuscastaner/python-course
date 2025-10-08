# for loop = do something a fixed number of times
#            you can iterate over a range, string, sequence, etc.

# count from 1 to 10
for x in range(1, 11):
    print(x)

# count from 10 to 1 (backwards)
for x in reversed(range(1, 11)):
    print(x)

# count every 5th number from 0 to 100
for x in range(0, 101, 5):
    print(x)

# count from 1 to 20 skipping number 13
for x in range(1, 21):
    if x == 13:
        print("...")
        continue
    else:
        print(x)

# count from 1 to 20 stopping right before number 13
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# nested loops (a loop within another loop)
# count from 1 to 10 three times
for x in range(3):
    print(f"Count no. {x + 1}:")

    for y in range(1, 11):
        print(y)

print("Done!")
