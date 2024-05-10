import sys
import os

def add(a,b):
    add = a+b
    return(add)

def sub(a,b):
    sub = a-b
    return(sub)

def mul(a,b):
    mul = a*b
    return(mul)
'''
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator == "add":
    output = add(a,b)
    print(output)

if operator == "sub":
    output = sub(a,b)
    print(output)

if operator == "mul":
    output = mul(a,b)
    print(output)
'''

print(os.getenv("password"))
print(os.getenv("apitoken"))
