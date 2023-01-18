l=[]
n=int(input("How many elements? "))
for i in range(n):
    x=int(input("Enter element:"))
    l.append(x)
print("The list is:",l)
print("The maximum element in the list is:",max(l))
print("The minimum element in the list is:",min(l))
x=int(input("Enter new element to be added:"))
i=int(input("Enter index:"))
l.insert(i,x)
x=int(input("Enter new element to be deleted:"))
if x in l:
    l.remove(x)
else:
    print(x,"not in list")
print("The list is now:",l)
