#Global Vars #0
x = "awesome" #global variable

def myFunc():
    print("Python is" + x) #we can apply to the insider as a child

myFunc() #calling the function

#Example #1
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #Output:Python is fantastic

myfunc()

print("Python is " + x) #output:Python is awesome

#example #2
#If you use the global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc() #this function changes the global var from "awesome" to "fantastic"

print("Python is " + x)