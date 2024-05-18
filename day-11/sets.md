
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

## Set Items ##

Set items are unordered, unchangeable, and do not allow duplicate values.

 
## Unordered ##

Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.


## Unchangeable ##

Set items are unchangeable, meaning that we cannot change the items after the set has been created.


## Duplicates Not Allowed ##

Sets cannot have two items with the same value. Duplicate values will be ignored:


## Get the Length of a Set ##

print(len(thisset))


## Set Items - Data Types ##

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}


## type() ##

From Python's perspective, sets are defined as objects with the data type 'set': <class 'set'>


## The set() Constructor ##

It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) 
print(thisset)


## Set Operations ##

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

my_set.add(6) #adding the item
my_set.remove{3} #removing the item
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
