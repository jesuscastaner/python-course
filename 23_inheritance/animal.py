# these are example classes

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


# both child and parent classes
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# child classes (multilevel inheritance)
class Dog(Predator):
    def speak(self):
        print(f"Woof!")


class Cat(Prey, Predator):  # multiple inheritance
    def speak(self):
        print(f"Meow!")


class Mouse(Prey):
    def speak(self):
        print(f"Squeek!")
