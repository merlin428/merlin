#def add(num1,num2):
 #   return num1+num2
#res=add(10,20,30,40)  #more than two arguments are not supported here.
#print(res)


#def add(*args):
 #   print(args)

  #  add(10,20,30,40,50)  #using args we can add many values
                         #(*args) accepts using tuple format


def add(*args):
    total=0
    for num in args:
        total+=num
    print(total)

add(10,20,30,40)

def print_emp_data(**args):
    for k,v in args.items():
        print(k,v)
print_emp_data(eid=100,job="kakkanad",resid="ernakulam")
