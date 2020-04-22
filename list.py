"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

# List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[1])
# last item
print(thislist[-1])

#range
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Change value item
thislist[1] = "ca chua"
print(thislist)


# Loop Through a List
for x in thislist:
    print(x)

# Check if Item exists

if "ca chua" in thislist:
    print('Co ca chua')

# list length
print(len(thislist))

# add Item

thislist.append("dao")
print(thislist)

# To add an item at the specified index, use the insert() method:

thislist.insert(1, 'Hahah')
print(thislist)

# REMOVE ITEM
thislist.remove("apple")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified):

thislist.pop()
print(thislist)

# The del keyword removes the specified index:

del thislist[0]
print(thislist)

thislist2 = ["apple", "banana", "cherry"]
del thislist2

#The clear() method empties the list:
thislist.clear()
print(thislist)

#copy
thislist3 = ["apple", "banana", "cherry"]
mythislist = thislist3.copy()
print(mythislist)

#Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)