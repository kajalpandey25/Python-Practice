class Employee:
    def __init__(self):
        self.__name = "Kajal"

a = Employee()
# print(a.name)
# print(a.__name) # Cannot be accessed directly
print(a._Employee__name) # Can be accessed indirectly
print(a.__dir__()) 



class Student:
    def __init__(self):
        self._name = "Khushi"

    def _funName(self):      # protected method
        return "CodeWithKhushi"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())