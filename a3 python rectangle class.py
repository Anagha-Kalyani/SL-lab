class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

l1=int(input("Enter length of first rectangle: "))
b1=int(input("Enter length of first rectangle: "))
r1=rectangle(l1,b1)
print("Area of the rectangle is: ",r1.area())
print()
l2=int(input("Enter length of second rectangle: "))
b2=int(input("Enter length of second rectangle: "))
r2=rectangle(l2,b2)
print("Area of the rectangle is: ",r2.area())
