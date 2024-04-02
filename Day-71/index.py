# dir() method

x = [1, 2, 3]
print(dir(x))
print(x.__add__)


# __dict__ attribute

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("Kajal", 22)
print(p.__dict__)

#  help() mehthod
print(help(Person))
