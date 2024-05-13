#list

A list is a fundamental data structure in programming that allows you to store a collection of items. Lists are ordered and can contain elements of various data types, such as numbers, strings, and objects.
my_list = [1, 2, 3, 'apple', 'banana']

List elements are indexed, starting from 0 for the first element. You can access elements by their index.

first_element = my_list[0]

You can find the length of a list using the len() function.
list_length = len(my_list) 

You can add elements to the end of a list using the append() method.
my_list.append(4)

You can remove elements by their value using the remove() method.
my_list.remove('apple')

Slicing allows you to create a new list from a subset of the original list.
subset = my_list[1:4]

You can combine two or more lists to create a new list.
new_list = my_list + [5, 6]

You can sort a list in ascending or descending order using the sort() method.
my_list.sort() 

You can check if an element exists in a list using the in keyword.
is_present = 'banana' in my_list 


