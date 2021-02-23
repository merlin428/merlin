employees={
    1000:{"eid":1000,"ename":"raj","desig":"developer","salary":20000},
    1001:{"eid":1001,"ename":"ram","desig":"tester","salary":25000},
    1002:{"eid":1002,"ename":"shyam","desig":"tester","salary":30000},
}

eid=int(input("enter eid"))
property=input("enter property value")
if eid in employees:
    print(employees[eid]["salary"])
    if property in employees[eid]:
        print(employees[eid][property])
    else:
        print("invalid property")
else:
    print("invalid employee")
