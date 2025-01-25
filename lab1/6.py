#Strings

#they're both are same
print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#This won't work as u planned
a2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a2)

#String with arrays
a = "Hello, World!"
print(a[1]) #output: e

#Strings Through looping
for x in "banana":
  print(x)

#String length
a1 = "Hello, World!"
print(len(a1))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Example
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Checking if Not
txt = "The best things in life are free!"
print("expensive" not in txt)

#Slicing
b = "Hello, World!"
print(b[2:5])

#Upper case
a = "Hello, World!"
print(a.upper())
#Concatination
a = "Hello"
b = "World"
c = a + b
print(c)

#f format
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#placeholder
price = 59
txt = f"The price is {price} dollars"
print(txt)

#escapeing characters
txt = "We are the so-called \"Vikings\" from the north."

#reomving whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#rapacing
a = "Hello, World!"
print(a.replace("H", "J"))

#Splitting
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#conc
a = "Hello"
b = "World"
c = a + " " + b
print(c)