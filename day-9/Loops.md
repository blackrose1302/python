## Loops in Python (for and while) ##

In Python, loops are used to execute a block of code repeatedly under certain conditions. There are two main types of loops: "for" loops and "while" loops.

FOR Loop:

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

WHILE Loop

The "while" loop continues to execute a block of code as long as a specified condition is true. It's often used when you don't know in advance how many times the loop should run.

count = 0
while (count < 3):
    count = count + 1
    print("Hello python user")

## Loop Control Statements (break and continue) ##

The BREAK Statement

With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

The CONTINUE Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


