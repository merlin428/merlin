texts="hello hai hello hai hello"
words=texts.split(" ")
dict={}
for word in words:
    if word not in dict:
       dict[word]=1
    else:
        dict[word]+=1
print(dict)
