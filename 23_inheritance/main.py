# inheritance            = allows a class to inherit attributes and methods from another class (parent)
#                          B(A)
# multiple inheritance   = inherit from more than one parent class
#                          C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
# super()                = function used in a child class to call methods from a parent class
# method overriding      = when a child class defines a method with the same name as one in the parent class
#                          the child's version replaces (overrides) the parent's version when called
#                          allows the child to customize or extend parent behavior
# polymorphism           = the ability for different classes to be used interchangeably, even if they behave differently
#                          an object could be treated of the same type as its parent class
#                          isinstance()

# inheritance
from animal import *

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)  # inherited attributes (just the fields, not the values)
print(cat.name)
print(mouse.name)

dog.eat()  # inherited methods
cat.eat()
mouse.eat()
dog.sleep()
cat.sleep()
mouse.sleep()

dog.speak()  # unique methods
cat.speak()
mouse.speak()

dog.hunt()  # dog can't flee
mouse.flee()  # mouse can't hunt
cat.flee()  # cat can do both (multiple inheritance)
cat.hunt()

# super()
from shape import *

circle = Circle(color="red", radius=5)
square = Square(color="blue", side=6)
triangle = Triangle(color="yellow", base=7, height=8)
marble = Marble(color="purple", pattern="striped")

print(circle.color)
print(square.color)
print(triangle.base)
print(triangle.height)
print(marble.color)
print(marble.pattern)

# overriding methods
circle.describe()  # uses parent's method
square.describe()  # uses parent's method
triangle.describe()  # uses child's method (overriden)
marble.describe()  # uses child's method (overriden)

# polymorphism
shapes = [Shape("orange"), circle, square, triangle, marble]

for item in shapes:
    print("---------------------")
    item.describe()
    print(f"Is it a Shape?: {isinstance(item, Shape)}")
    print(f"Is it a Circle?: {isinstance(item, Circle)}")
    print(f"Is it a Square?: {isinstance(item, Square)}")
    print(f"Is it a Triangle?: {isinstance(item, Triangle)}")
    print(f"Is it a Marble?: {isinstance(item, Marble)}")
