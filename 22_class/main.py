# object             = a "bundle" of related attributes (variables) and methods (functions)
# class              = blueprint that defines the structure and behaviour of an object
#                      you need a class to create objects (instances)
# instance variables = unique to each object, defined inside the constructor
# class variables    = shared among all instances of a class, defined outside the constructor

# define a class in a separate file; then import it
from car import Car

# create an object using its constructor
car1 = Car("Renault Clio",
           "2022",
           "white",
           15000,
           True)
car2 = Car("Seat Ibiza",
           "2020",
           "yellow",
           7000,
           False)

# access its attributes
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.price)
print(car1.is_new)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.price)
print(car2.is_new)

# access its methods
car1.drive()
car1.stop()

car2.drive()
car2.stop()

# instance and class variables
from student import Student

student1 = Student("Jesus", 29)
student2 = Student("Paula", 33)

print(student1.name)  # instance variables
print(student1.age)
print(student2.name)
print(student2.age)

print(Student.class_year)  # class variables
print(Student.num_students)

student3 = Student("David", 25)
print(Student.num_students)
