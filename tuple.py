# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.


thisistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisistuple[1])
print(thisistuple[-1])
print(thisistuple[2:5])

"""
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""


"""
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
"""
thisistuple = tuple(("apple", "banana", "cherry"))
print(thisistuple)