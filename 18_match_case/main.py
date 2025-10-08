# match-case statement = an cleaner and more readable alternative to using many elif statements
#                        executes some code if a value matches a 'case'
#                        similar to switches in other programming languages

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Unknown"


print(day_of_week(1))
print(day_of_week(3))
print(day_of_week("asdf"))  # Unknown


def is_pizza_day(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False


print(is_pizza_day("Monday"))
print(is_pizza_day("Tuesday"))
print(is_pizza_day("Wednesday"))
print(is_pizza_day("Thursday"))
print(is_pizza_day("Friday"))
print(is_pizza_day("Saturday"))
print(is_pizza_day("Sunday"))
print(is_pizza_day("asdf"))
