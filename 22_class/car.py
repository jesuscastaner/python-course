# this is an example class

class Car:
    # constructor (special method used to create objects)
    def __init__(self, model, year, color, price, is_new):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.is_new = is_new

    # custom methods
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")
