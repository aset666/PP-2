class MyClass:
  x = 5
print(MyClass)
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1=person("Sara", 21)
print(p1.name)
print(p1.age)

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=person("ceb", 22)
print(p1)

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1=person("noob", 12)
p1.myfunc()

