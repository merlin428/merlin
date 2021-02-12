arr1=[1,2,3,4,5,]
arr2=[1,2,4,5]
res=[]
for i in arr1:
    if i in arr2:
        res.append(i)
print(res)