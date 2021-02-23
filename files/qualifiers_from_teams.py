f1=open("teams","r")
f2=open("drop","r")

st1=set(f1)
print(st1)
st2=set(f2)
print(st2)

qualifier=st1.difference(st2)
print(qualifier)