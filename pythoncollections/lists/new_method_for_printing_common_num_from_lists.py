list1=[10,20,21,22,23]
list2=[8,9,20,21,25]
pos1=0
pos2=0
while((pos1<len(list1))&(pos2<len(list2))):
    if list1[pos1]==list2[pos2]:
        print(list1[pos1])
        pos1+=1
        pos2+=1
    elif list1[pos1]>list2[pos2]:
        pos2+=1
    else:
        pos1+=1