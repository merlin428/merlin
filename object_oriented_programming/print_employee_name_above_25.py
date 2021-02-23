class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
p=person(27,"ram")
p1=person(26,"varun")
p2=person(24,"nikhil")

employees=[]
employees.append(p)
employees.append(p1)
employees.append(p2)

for emp in employees:
    if emp.age>25:
        print(emp.name)

