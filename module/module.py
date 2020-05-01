'''
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''
# rename
import mymodule  as mx
import platform

mx.greeting("hahaha")


a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

# List all the defined names belonging to the platform module:
print(dir(platform))