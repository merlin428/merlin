class employee:
    company_name="dell"

    def __init__(self,age,name):
        self.age=age
        self.name=name
    def print_person(self):
        print(self.age)
        print(self.name)
        print(employee.company_name)
emp=employee(25,"merlin")
print(emp.name)
print(employee.company_name)