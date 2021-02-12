arr=[10,11,12,13,14]
element=int(input("enter the element for srch"))

flg=0
for num in arr:
    if(element==num):
        flg=1
        break

if flg==0:
    print("element not found")
else:
    print("element found")
