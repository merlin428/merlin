employees=[
    [100,"rincy","developer",25000,1989,1999],
    [101,"merlin","tester",24000,1990,2005],
    [102,"anjana","developer",23000,1975,1988],
    [103,"amla","testing",23000,1990,1999],
]
highest_experience=[]
for employee in employees:
    highest_experience.append(employee[5]-employee[4])
print("employee=",max(highest_experience))
print(highest_experience)