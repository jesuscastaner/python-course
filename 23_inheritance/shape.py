# these are example classes

class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"This shape is {self.color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def describe(self):  # overriding parent's method
        super().describe()
        print(f"It's a beautiful triangle!")  # extends its functionality


class Marble(Circle):  # a Marble is a Marble, a Circle and a Shape (polymorphism)
    def __init__(self, color, pattern):
        super().__init__(color, 1.5)
        self.pattern = pattern

    def describe(self):
        print(f"A {self.color} marble with a {self.pattern} pattern")
