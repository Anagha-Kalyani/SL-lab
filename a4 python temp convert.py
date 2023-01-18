def ctof(c):
    return (c*9/5)+32
def ftoc(f):
    return (f-32)*5/9
def ctok(c):
    return c+273
def ktoc(k):
    return k-273
def ftok(f):
    return ctok(ftoc(f))
def ktof(k):
    return ctof(ktoc(k))
ans='y'
l=[]
print("MENU\n\
1. c to f\n\
2. f to c\n\
3. c to k\n\
4. k to c\n\
5. k to f\n\
6. f to k")
while(ans=='y'):
    ch=int(input("Enter choice"))
    if ch==1:
        x=int(input("Enter temp:"))
        tup=(x,ctof(x))
        l.append(tup)
        print(ctof(x))
    elif ch==2:
        x=int(input("Enter temp:"))
        tup=(x,ftoc(x))
        l.append(tup)
        print(ftoc(x))
    elif ch==3:
        x=int(input("Enter temp:"))
        tup=(x,ctok(x))
        l.append(tup)
        print(ctok(x))
    elif ch==4:
        x=int(input("Enter temp:"))
        tup=(x,ktoc(x))
        l.append(tup)
        print(ktoc(x))
    elif ch==5:
        x=int(input("Enter temp:"))
        tup=(x,ftok(x))
        l.append(tup)
        print(ftok(x))
    elif ch==6:
        x=int(input("Enter temp:"))
        tup=(x,ktof(x))
        l.append(tup)
        print(ktof(x))
    else:
        print("Invalid input")
    ans=input("Do you wish to continue(y/n)")
print("The list is: ",l)
p=int(input("Sort by ele 1 or ele 2?"))
if p==1:
    print(sorted(l,key=lambda x:x[0]))
else:
    print(sorted(l,key=lambda x:x[1]))
