
####### string inbuilt functions which are used mostly #######

# print the string

a = " The author"
b = "new "

c = a + " is " + b 
print ("New concat string is ", "\n\n" ,c)
 
print ("the length od string is ",len(c))

uc = b.upper()
lc = b.lower()

print ("Uppercase : ", uc )
print ("Lowercase : ", lc)

d = c.replace ("new", "xyz")

print ("Replaced String : ", d)

# The split() method returns a list where the text between the specified separator becomes the list items.

e = d.split()
print ("Words : ", d)

# The strip() method removes any whitespace from the beginning or the end:

print(c.strip())

substring = "new"
if substring in c:
    print(substring, "found in the text")

