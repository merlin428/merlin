f=open("content","r")
word=[]
set=[]
for lines in f:
    set.append(lines.rstrip("\n"))
for words in set:
    word+=words.split(" ")
print(word)
