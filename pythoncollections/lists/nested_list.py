employees=[
    [100,"merlin","analyst",30000],
    [101,"mebin","developer",20000],
    [102,"james","developer",12000],
    [103,"suby","tester",12000]
]
#print employee names

for employee in employees:
    print(employee[1])

#print employee names those who are developers

for employee in employees:
    if employee[2]=="developer":
       print(employee)

#print the total salary of all employees

total=0
for salary in employees:
    total+=employee[3]
print("total=",total)

#print the highest salary from the employees using max function

sallist=[]
for emp in employees:
    sallist.append(emp[3])
print("high sal=",max(sallist))



