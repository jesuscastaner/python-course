# static method = a method that belongs to the class itself rather than any particular instance
#                 (as opposed to instance method)
# class method  = a method that allows operations related to the class itself
# magic method  = also called "dunder" (double underscore) methods
#                 automatically invoked by python's built-in operations


class Employee:
    count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    # static method
    @staticmethod
    def is_valid_position(position):
        return position in ["CEO", "Manager", "Senior Developer", "Junior Developer"]

    # class method
    @classmethod
    def get_count(cls):
        if cls.count <= 0:
            return f"There are no employees..."
        elif cls.count <= 2:
            return f"There are only {cls.count} employees..."
        else:
            return f"Wow! There are {cls.count} employees!"

    # magic methods
    def __str__(self):
        return f"{self.name} works as a {self.position}"

    def __eq__(self, other):
        return self.name == other.name and self.position == other.position and self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __add__(self, other):
        return self.salary + other.salary

    def __contains__(self, keyword):
        return keyword.lower() in self.position.lower() or keyword in self.name.lower()

    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "position":
            return self.position
        elif key == "salary":
            return self.salary
        else:
            return f"Key '{key}' not found"


# static method
print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Architect"))

# class method
print(Employee.get_count())

employee1 = Employee("Jesus", "Junior Developer", 40000)
employee2 = Employee("Paula", "CEO", 250000)
print(Employee.get_count())

employee3 = Employee("David", "Senior Developer", 80000)
print(Employee.get_count())

# magic methods
print("__str__")
print(employee1)
print(employee2)
print(employee3)

print("__eq__")
print(employee1 == Employee("Laura", "Junior Developer", 40000))
print(employee1 == Employee("Jesus", "Senior Developer", 40000))
print(employee1 == Employee("Jesus", "Junior Developer", 31000))
print(employee1 == Employee("Jesus", "Junior Developer", 40000))

print("__lt__")
print(f"-> Does {employee1.name} earn more than {employee2.name}?")
print(employee1 < employee2)
print(f"-> Does {employee2.name} earn more than {employee3.name}?")
print(employee2 < employee3)

print("__gt__")
print(f"-> Does {employee1.name} earn less than {employee2.name}?")
print(employee1 > employee2)
print(f"-> Does {employee2.name} earn less than {employee3.name}?")
print(employee2 > employee3)

print("__add__")
print(employee1 + employee2)
print(employee2 + employee3)

print("__contains__")
print("dEVeLoP" in employee1)
print("pau" in employee1)
print("asdf" in employee3)

print("__getitem__")
print(employee1["name"])
print(employee2["position"])
print(employee3["salary"])
print(employee3["asdf"])
