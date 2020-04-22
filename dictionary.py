# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdic = {
    "brand" : 'Vinfast',
    "model": "Lux SA",
    "year": 2108
}

x = thisdic["brand"]
print(x)

# Change value
thisdic["year"] = 2020
print(thisdic)


for x in thisdic:
    print(x)
    print(thisdic[x])

for x in thisdic.values() :
    print(x)
if "model" in thisdic:
    print("Yes, model is one of the keys in the thisdic dictionary ")

print(len(thisdic))

thisdic["color"] = "Red"
print(thisdic)

event = {
    'UpdateRecruit': True
}
if ('UpdateRecruit' in event):
    print('In ne')