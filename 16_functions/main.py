# function        = a block of reusable code that performs a task
#                   defined with 'def' and called by using ()
# return          = ends a function and optionally sends a value back to the caller
# params          = input values defined in the function def
# args            = values passed to the function when calling it
# positional args = args matched to params based on their order
# default args    = params with default values used if no argument is provided
# keyword args    = args passed by explicitly naming the param; order doesn't matter
# arbitrary args  = allow passing an arbitrary quantity of positional (*args) or keyword (**kwargs) args
#                   use * as unpacking operator

# positional args
def happy_birthday(name, age):
    print(f"Happy birthday, {name}!")
    print(f"You are {age} years old")


happy_birthday("Jesus", 29)
happy_birthday(29, "Jesus")  # (!) the position of the params matter


def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of {amount:.2f}€ is due on {due_date}")


display_invoice("Jesus", 42.01, "01/06/2025")


# return
def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


num1 = 5
num2 = 2

print(add(num1, num2))
print(subtract(num1, num2))
print(multiply(num1, num2))
print(divide(num1, num2))


# default args
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(f"{net_price(500, 0.23, 0.1432):.2f} €")
print(f"{net_price(500, 0.5):.2f} €")
print(f"{net_price(500):.2f} €")


# keyword args
def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")


hello(title="Mr.", last_name="Castaner", first_name="Jesus", greeting="Hello")
hello(last_name="Castaner", title="Mr.", greeting="Hello", first_name="Jesus")


# arbitrary args (*args, **kwargs)
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(2, 3))
print(add(2, 3, 10, 500, -100))
print(add(1))
print(add())


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


print_address(street="Calle Mayor",
              number="3",
              zipcode="28000",
              city="Madrid",
              country="Spain")


# combined
def shipping_label(*args, **kwargs):
    print("------ SHIPPING LABEL ------")

    for arg in args:
        print(arg, end=" ")
    print()

    if "number" in kwargs:
        if "apartment" in kwargs:
            print(f"{kwargs.get('street')}, {kwargs.get('number')}, {kwargs.get('apartment')}")
        else:
            print(f"{kwargs.get('street')}, {kwargs.get('number')}")
    else:
        print(f"{kwargs.get('street')}, S/N")

    print(f"{kwargs.get('zipcode')} {kwargs.get('city')}")
    print(f"{kwargs.get('country').upper()}")


shipping_label("Don", "Jesus", "Castaner", "III",
               zipcode="28000",
               number="3",
               street="Calle Mayor",
               apartment="2ºA",
               country="Spain",
               city="Madrid")

shipping_label("Ms.", "Paula",
               street="Paseo del Pez",
               city="Valencia",
               number="16",
               country="Spain",
               zipcode="46000")

shipping_label("Ayuntamiento",
               country="Spain",
               street="Plaza del Ayto.",
               zipcode="08000",
               city="Barcelona")
