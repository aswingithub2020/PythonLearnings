from operator import truediv

import self

x=5
y="Hello world"
print (x)
x="Test"
print (y)
print (x)

#This is single line comment

"""
This is multi-line comment with triple quotes
"""

'''
This is multi-line comment with triple quotes
'''

#Type-Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

#String can be declared using single or double quotes
x='ABC'
y="XYZ"
print(x)
print(y)

#variable names are case sensitive
x="ABC"
X="XYZ"
print(x)
print(X)

#MultiWords Variable Names canbe declared as Pascal case MyVariableNam ,Camel Case myVariableNam, Snake Case my_variable_name

#Many values to multiple variables in single line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)
print(f"{x}\n{y}\n{z}") #output multiple variables using single print(), but prints in same line,
print(x,y,z, sep="\n")#use seperator for printing in different lines
print('Hello', 'World' ,sep=",") #o\p:--Hello,World

#Global Variables
x = "awesome" #Global variable
print (x)
def myfunc():
  z="dangerous" #local variable
  print("Python is " + x)
print (z)
myfunc()

#Global keyword
def myfunc1():
  global x
  x = "fantastic"
  print("myfunc1 x value "+x)

myfunc()
def myfunc2():
  print(x)

myfunc1()
myfunc2()

print("{Global keyword} Python is " + x)

#DataTypes
x="String"  # String
x=10  #int
x=1.2 #float
x=["Mango","apple","banana","cherry"] #list mutuable
print(x)
x=("Mango","apple","banana")  #Tuple immutable
print(x)
x = {"apple", "banana", "cherry"} #set mutable
x.add("Mango")
x.add("orange")
print(x)
x=True #bool
print(type(x))
x = frozenset({"apple", "banana", "cherry"}) #Frozenset Immutable
print(x)

#Specify DataType using Constructor functions
#int
x=int(10)
#loat
x=float(10.5)
#String
x=str("Hello World")
#List
x=list(("apple","Banana"))
#tupple
x=tuple(("apple","Mango"))
#dict
x=dict(name="Test",date=123)
#set
x=set(("apple","banana"))
print(x)
#bool
x=bool(True)
#float in scientific number
x = -87.700e100
print(x)
x =12E4 # or 12e4 both are same
print(x)

#Type Casting or COnversion
x=1 #int
y=1.2 #float
z=1+3j #complex
A="123"

#convert from int to float
a=float(x)
print(a)

#convert int to complex
b=complex(x)
print(b)

#convert float to int
c=int(y)
print(c)

#convert String  to int
d=int(A)
print(d)

#Random Number
import random
print(random.randrange(1,100))

#Quotes Inside Quotes
x="It's alright"
y='He is "superhero"'
print(x)
print(y)

#Multiline Strings---You can assign a multiline string to a variable by using three double/single quotes
x= '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(x)

#Character Array using String
a = "Hello, World!"
print(a[1])
print(len(a))

#Looping through String array
for x in "banana":
  print(x)

#Check sub-string presents in a String
x="This is India"
if"Indian" in x:
  print("'India' word presents in "+x)
else:
  print("'India' word not present in "+x)

#Check sub-string not presents in a String
x="This is Africa"
if "India" not in x:
  print("Word does not exist")
else:
  print("Word Exists")

#Slicing String
x="Perplexity Pro"
print(slice(x[3:6]))
print(x[:6])
print(x[2:])
c="Madam"
print(c[:-1])
print(c[-3:-1])

#Remove Whitespaces start and end of the string
a=" Hello "
print(a.strip())

#Replace String
a="Hello World"
print(a.replace('H','F'))

#Split String
a="Hello,World"
print(a.split(','))

#F-String
a=2025
b=f"This is Year {a:.2f}"
print(b)

txt = "We are the so-called Vikings from the north."
print(txt.title())


