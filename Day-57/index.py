class Person:
    name = "Kajal"
    occupation = "Software Developer"
    networth = 1000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Sonali"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"
# print(a.name, a.occupation) 
a.info()
b.info()
c.info()   