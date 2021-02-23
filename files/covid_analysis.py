f=open("covid_19_india(1).csv")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    state=data[3]
    confirmed_cases=int(data[-1])
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,"========>",v)

data=max(dict,key=dict.get)

print(data)




