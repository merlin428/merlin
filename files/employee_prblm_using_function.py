employees={
    1000:{"eid":1000,"ename":"raj","desig":"developer","salary":20000},
    1001:{"eid":1001,"ename":"ram","desig":"tester","salary":25000},
    1002:{"eid":1002,"ename":"shyam","desig":"tester","salary":30000},
}

#print_employee(eid=1000) employee name
#print_employee(eid=1000,property="salary")
#print_employee(eid=1000,property="desig")


def print_employee_details(**kwargs):    #kwargs=[eid:1000,property=salary]
    id=kwargs["eid"]  #1000

    if id in employees:
        print(employees[id]["ename"])
        prop=kwargs["property"] #salary
        print(employees[id][prop])
    else:
        print("id not exist")

print_employee_details(eid=1000,property="desig")
