i = 1
while i < 6:
    print(i)
    if 3 == i:
        break
    i+=1

x = 0
while x < 6:
    x+=1
    if 3 == x:
        continue
    print('x')
    print(x)

z = 1
while z < 6:
  print(z)
  z += 1
else:
  print("z is no longer less than 6")


'''
For loop
'''
fruits = ['Apple', 'Banana', 'Cherry']
for fruit in fruits:
    print(fruit)

# Loop through a string

for x in "thisisString":
    print(x)


for x in range(6):
    print(x)
else:
    print('Finally finished!')