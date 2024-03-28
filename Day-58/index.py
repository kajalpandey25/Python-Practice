class Person:
    def __init__(self, name, occ):
        print("Hey I am a Person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Kajal", "Developer")
b = Person("Divya", "HR")
c = Person("Abhi", "Game Developer")
a.info()
b.info()
c.info()
# # print(a.name) 
# a.name = "Divya"
# a.occ = "HR"
# a.info()       