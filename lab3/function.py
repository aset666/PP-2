"""
def myfunction():
    print("Hllo from a function")
myfunction()
"""


"""
def myfunction(fname):
    print(fname + " stark")
myfunction("Emil")
myfunction("Tobias")
myfunction("Linus")
"""
"""
def mira(fname, lname):
    print(fname+" "+lname)
mira("Asd", "Dsa")
"""

#Arbitrary Arguments, *args
"""
def mir(*kids):
    print("The youngest child is " + kids[2])
mir("Emil", "Tobias", "Linus") 
"""

"""
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
def ss(a,b):
    return((2*a)+(4*b))
print(ss(a,b))
"""
"""
def s(name, age):
    print("Name: ", name)
    print("Age: ", age)
s("Mira", 20)
"""
"""
def s(name="world"):
    print(f"Hello", name)
s()
"""
def s(*name):
    return sum(name)
print(s(1,2,3,4,5))
