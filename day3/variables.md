
Python Variable is containers that store values. A Python variable is a name given to a memory location. It is the basic unit of storage in a program.

## variable creation 

Python has no command for declaring a variable. Variables do not need to be declared with any particular type, and can even change type after they have been set.

Variable names are case-sensitive.

## Variable Names

Rules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores.
4. Variable names are case-sensitive 
5. A variable name cannot be any of the Python keywords.

## Multi Words Variable Names

Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:

1. myVariableName = "John" (Camel Case)
2. MyVariableName = "John" (Pascal Case)
3. my_variable_name = "John" (Snake case)

## Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry" (here x = Orange , y = Banana, z= Cherry)
x = y = z = "Orange" (here all three variables has same value)

You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  == > Python is awesome 

## Global Variables

Variables that are created outside of a function are known as global variables. Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()    ==> Python is awesome

## local variables

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)   ==> Python is fantastic
                              Python is awesome

## global Keyword

To create a global variable inside a function, you can use the global keyword.
Also, use the global keyword if you want to change a global variable inside a function.  

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)    == > Python is fantastic
