i=1
n=int(input("enter the limit to be sum:"))
ototal=0
etotal=0
while i<=n:
    if (i % 2 ==0):
        etotal = etotal+i
    else:
        ototal=ototal+i
    i+=1
    print("total of even no.s",etotal)
    print("total of odd no.s",ototal)

