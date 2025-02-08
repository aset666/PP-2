"""
x=lambda a:a+15
print(x(5))
"""
"""
x=lambda a,b:a*b
print(x(5,6))
"""

"""
def mir(n):
    return lambda a:a*n
    d=mir(5)
    print(d(10))
"""
    
def mir(n):
    return lambda a:a*n
d=mir(5)
print(d(10))

def mir(n):
    return lambda a:(a*n)%2
d=mir(5)
b=mir(7)
print(d(7))   
print(b(7))
