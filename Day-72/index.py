# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass): 
#     def parent_method(self):
#         print("Kajal")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

sonam = Employee("sonam Pandey", "1")
kajal = Programmer("Kajal Pandey", "2", "Python")   
print(kajal.name)
print(kajal.id)
print(kajal.language)         