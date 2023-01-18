class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(self.name,self.age,self.marks)
    def accept(self):
        self.name=input("Enter name")
        self.age=input("Enter age")
        m1=input("Enter marks for sub 1")
        m2=input("Enter marks for sub 2")
        m3=input("Enter marks for sub 3")
        self.marks=[m1,m2,m3]
stu1=student("alice",20,[90,90,100])
stu1.display()
stu2=student('',0,[])
stu2.accept()
stu2.display()
