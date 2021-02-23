#id,name,total,set_student,print_student


class student:
    def set_student(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
    def print_student(self):
        print(self.id)
        print(self.name)
        print(self.total)

obj1=student()
obj1.set_student(11,"shyam",80)
obj1.print_student()