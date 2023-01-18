from functools import reduce
l=[]
print("Enter list elements: ")
for i in range (0,6):
    num=int(input("Enter element: "))
    l.append(num)
print("The list is: ",l)
l2=[i*3 for i in l]
print("The new list is: ",l2)
sum1=reduce(lambda x,y: x+y,l)
sum2=reduce(lambda x,y: x+y,l2)
print("The sum of elements in original list is: ",sum1)
print("The sum of elements in the new list is: ",sum2)

