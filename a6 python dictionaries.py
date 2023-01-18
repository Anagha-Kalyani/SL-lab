def AtomicDictionary():
    elements={'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Beryllium','B':'Boron'}
    print("The dictionary is:",elements)
    n=int(input("How many more elements would you like to add? "))
    for i in range(0,n):
        print("Enter details of element",i+1,":")
        key1=input("Enter the key:")
        if key1 in elements:
            print("Warning: Key already exists in dictionary. Existing value will be rewritten with new value.")
        val1=input("Enter the value:")
        elements[key1]=val1
        """unique key- append,
    duplicate key- rewrite"""
    print("The dictionary is:",elements)
    print("The number of elements in the dictionary is",len(elements))
    key=input("Enter the symbol of element to be searched in the dictionary:")
    if key in elements:
        print("The element is present in the list with key",key,"and value",elements[key])
    else:
         print("Element is not found in list.")

"""
from a6 import *
AtomicDictionary()
"""
