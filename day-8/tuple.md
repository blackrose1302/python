#tuple
 
Tuple is a data structure similar to a list, but unlike lists, tuples are immutable, meaning their contents cannot be changed after creation. Tuples are typically used for grouping related data.

You can create a tuple in various programming languages. In Python, for example, you create a tuple using parentheses:

my_tuple = (1, 2, 'apple', 'banana')

Tuple elements are indexed, starting from 0 for the first element. You can access elements by their index, just like lists.

first_element = my_tuple[0] 

You can find the length of a tuple using the len() function.

tuple_length = len(my_tuple)

Tuples are immutable, so you can only access their elements.

second_element = my_tuple[1]

You can pack multiple values into a tuple and unpack them into separate variables.

coordinates = (3, 4)
x, y = coordinates  

You can concatenate two or more tuples to create a new tuple.
new_tuple = my_tuple + (3.14, 'cherry')

You can check if an element exists in a tuple using the in keyword.
is_present = 'apple' in my_tuple

Tuples are often used to return multiple values from a function.
def get_coordinates():
    return (3, 4)

x, y = get_coordinates() 
 