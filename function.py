def myFunction():
    print("Hello function")

myFunction()


# Arbitrary Arguments, *args
def functionLala(*kids): 
    print(kids[1])

functionLala("aaa", "dddd")

#Keyword Arguments
def keywordArg(child3, child2, child1):
    print("The youngest child is " + child3)
keywordArg(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#unknow keywork arg
def unknow_function(**kid):
  print("His last name is " + kid["lname"])

unknow_function(fname = "Tobias", lname = "Refsnes")
