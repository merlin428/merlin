arr=[10,12,11,13,15,14]
elmnt=int(input("enter the number"))
arr.sort()
flg=0
low=0
upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2

    if (elmnt>arr[mid]):
        low=mid+1
    elif(elmnt<arr[mid]):
        upp=mid-1
    elif(elmnt==arr[mid]):
        flg=1
        break
if (flg==0):
    print("element not found")
else:
    print("element found")





