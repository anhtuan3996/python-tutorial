print(10>9)
print(9>10)
print(9 == 10)

# condition in an if statement
a = 2000
b = 300

if a > b:
    print("A lon hon b ne")
else:
    print("A khong lon hon b ne,hihihi")

'''
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,
'''
print(bool("hello"))
print(bool(15))
# false value
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# function return boolean
def myFunction() :
    return True

print('Function')
print(myFunction())

if myFunction() :
    print('Function true ne')
else :
    print('Function la false ne')

# Check if an object is an integer or not:
x = 100
print(isinstance(x, int))