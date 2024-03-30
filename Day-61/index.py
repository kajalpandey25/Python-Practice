class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_details(self):
        print(f"The name of Employee: {self.employee_id} is {self.name}")  


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

        
e1 = Employee("Kajal Pandey", 320)
e1.show_details()
e2 = Programmer("Abhi", 400)
e2.show_details()
e2.showLanguage()
