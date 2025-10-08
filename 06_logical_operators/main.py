# logical operators = evaluate multiple conditions
#                     or  = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temperature = 25
is_windy = True
is_sunny = True

# or
# (the event is cancelled if it’s too hot, too cold, or windy)
if temperature >= 28 or temperature < 10 or is_windy:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and
# (describe the weather if it's sunny)
if temperature >= 28 and is_sunny:
    print("It's hot and sunny outside")
elif 0 < temperature < 28 and is_sunny:
    print("It's warm and sunny outside")
elif temperature <= 0 and is_sunny:
    print("It's cold but sunny outside")
else:
    print("It's not sunny outside")

# not
# (decide whether you need an umbrella based on whether it's sunny or not)
if not is_sunny:
    print("You should take an umbrella")
else:
    print("You don't need an umbrella")

# combining or, and, not
if 10 < temperature < 28 and (not is_windy or is_sunny):
    print("Nice weather for outdoor activities!")
else:
    print("The weather is not good for outdoor activities")
