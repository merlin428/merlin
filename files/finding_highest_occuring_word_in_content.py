f=open("content","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,",",v)
word=sorted(dict,key=dict.get,reverse=True)
print("sorted values=",words)