class Person:
    def set_Person(self,name,age):
        self.name=name
        self.age=age
    def print_Person(self):
        print(self.name)
        print(self.age)

obj=Person()
obj.set_Person("ram",23)
obj.print_Person()