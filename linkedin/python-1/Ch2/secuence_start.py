# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print("length of list: ",len(mylist))

# to access a member of a sequence type, use []
print("index 2, third item ->",mylist[2])
print("index -1, from the end ->",mylist[-1])
# mylist[0] = 10
# print(mylist)

# add a list to another list
# another_list = [6,7,8]
# mylist = mylist + another_list
print("COMPLETE LIST", mylist) #add lists

mystr = "This is a string" #strings are immutable
print(mystr[2]) 
# mystr[2] = "Z" # gives error

# use slices to get parts of a sequence

print("slices of string:", mylist[1:4])
print("slices of string stepping:", mylist[1:4:2])
print("slices of string stepping 1:", mylist[::2])

# you can use slices to reverse a sequence
print("reversing list: ",mylist[::-1])

# Tuples are like lists, but they are immutable
mytuple = (0, 1, 2, "three")
print(mytuple)
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = { 1, 2, 3, 2, 4, "hey" }
print(myset) #repeated values get filtered out

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print("is 1 in list",1 in mylist)
print("is 3 in tuple",3 in mytuple)
print("is 5 in set",5 in myset)