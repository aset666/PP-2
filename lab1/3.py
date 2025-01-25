#Variables
#Legal variable names
myvar="Asd"
my_var="Qw"
_my_variable="Nuri"
myVar="qwe"
MYVAR2323="QWE"
MYVAR="12321"
myvar12="12ws"

#Illegal var  names
# 2myvar="123"
# my-var = "John"
# my var = "John"

#camelCase
myVarName = "Asad"

#PascalCase
MyVar="Nuras"

#snake_case
my_var_name="asdzxc"

#Many Values to Multiple Variables
x1,y1,z1="Orange", "Yellow", "Blue"
print(x1)
print(y1)
print(z1)

#One Value to Multiple Variables
x2=y2=z2 = "all the same"
print(x2)
print(y2)
print(z2)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x3, y3, z3 = fruits

print(x3)
print(y3)
print(z3)

#OutPut Var
x4 = "Python"
y4 = "is"
z4 = "awesome"
print(x4, y4, z4)

x5 = "Python "
y5 = "is "
z5 = "awesome"
print(x5 + y5 + z5)

#We can sum int
x = 5
y = 10
print(x + y)

#We can't sum string and INT vars
x = 5
y = "John"
print(x + y)
#THIS IS COMPLETALY WRONG

#THIS IS THE RIGTH WAY
x = 5
y = "John"
print(x, y)