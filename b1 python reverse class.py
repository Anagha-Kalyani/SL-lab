class reverse:
    def __init__(self,string):
        self.string=string
    def rev(self):
        str1=self.string
        list1=str1.split()
        listr=list1[::-1]
        strrev=" ".join(listr)
        print(strrev) 
    def countvowel(self):
        count=0
        for i in range(0,len(self.string)):
            if(self.string[i].lower() in ['a','e','i','o','u']):
                count+=1
        return count
        
s1=input("String 1:")
s2=input("String 2:")
s3=input("String 3:")

a=reverse(s1)
b=reverse(s2)
c=reverse(s3)


print("\nThe reversed strings:\n")
a.rev()
b.rev()
c.rev()

x=[]
x.append((a.countvowel(),a.string))
x.append((b.countvowel(),b.string))
x.append((c.countvowel(),c.string))

x=sorted(x,key=lambda x:x[0],reverse=True)
print("\nThe strings in decreasing order of number of vowels:\n")
for i in range(0,3):
    print(x[i][1],"\t-",x[i][0],"vowels")
