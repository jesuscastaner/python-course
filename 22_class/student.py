# this is an example class

class Student:
    class_year = 2025  # class variable
    num_students = 0  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable
        Student.num_students += 1
