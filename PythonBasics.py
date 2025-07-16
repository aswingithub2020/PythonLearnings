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
x=["Mango","apple","banana","cherry"] #list
print(x)
x=("Mango","apple","banana")  #Tuple
print(x)
x = {"apple", "banana", "cherry"} #set
x.add("Mango")
x.add("orange")
print(x)


