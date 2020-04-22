# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.



thisset = { "apple", "banana", "cherry" }
print(thisset)

for x in thisset:
    print(x)

#Check if "banana" is present in the set:

print("banana" in thisset)

'''
Change Items
Once a set is created, you cannot change its items, but you can add new items.

'''


"""
Add Items
To add one item to a set use the add() method.

To add more than one item to a set use the update() method.
"""
thisset2 = {"apple", "banana", "cherry"}
thisset2.add("orange")
print(thisset2)


thisset3 = {"apple", "banana", "cherry"}
thisset3.update(["orange", "mango", "grapes"])
print(thisset3)


print(len(thisset3))

#Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisset.remove("apple")
print(thisset)
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)