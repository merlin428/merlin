#key id name designation salary
#print employee salary
#employee salary
#check for gender key if not add gender key value pair
#iterate all key value pairs

employee={"name":"rincy","id":100,"design":"developer","salary":25000}
print(employee["name"])

print(employee["salary"])

if "gender" in employee:
    print("allready exist")
else:
    employee["gender"]="female"
print(employee)

for k,v in employee.items():
    print(k,",",v)
