f=open("demo","r")
lst=[]

for lines in f:
    print(lines)

    lst.append(lines.rstrip("\n"))
print(lst)

st=set(lst)
print(st)




name="luminar"
name.rstrip("\n")
print(name)

