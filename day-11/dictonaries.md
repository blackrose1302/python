

Dictionaries are used to store data values in key:value pairs. 
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:

Eg: 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

## Dictionary Items ##

Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
and can be printed as

  print(thisdict["brand"])

## Ordered or Unordered? ##

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

## Changeable ##

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

## Duplicates Not Allowed ##

Dictionaries cannot have two items with the same key. Duplicate values will overwrite existing values:

## Dictionary Length ##

To determine how many items a dictionary has, use the len() function:
    print(len(thisdict))


## Dictionary Items - Data Types ##

The values in dictionary items can be of any data type: String, int, boolean, and list data types:



## type() ##

From Python's perspective, dictionaries are defined as objects with the data type 'dict': <class 'dict'>

## The dict() Constructor ##

It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


########### Python Collections (Arrays) ###########

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


