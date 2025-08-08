# Basic data types in Python: Numbers, Strings and Booleans
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
# print(myint)
# print(mystr)


# Operators are used to perform operations on variables
print("addition: ", myint + myfloat)
print("multiplication: ", myint * myfloat)
print("division: ", myint / myfloat)
print("module operator: ", myint % 3) #gives me the remainder of the first number divided by the second
print("-" * 20)

another_str = "- This is another string"

print(mystr + another_str) #chain strings
print("nom " * 3)
print("-" * 20)

# Logical and comparison operators 
print("equal: ", myint == 10)
print("notequal: ", myfloat != 20)
print("greater than: ", myint > 10)
print("less than: ", myint < 10)
print("-" * 20)

print("and: ",myint > 5 and myfloat < 25.0)
print("or: ",myint < 5 or myfloat < 25.0) #only one needs to be true
print("not: ", not (myint < 5 or myfloat < 25.0)) #flips the boolean value
print("-" * 20)

# re-declaring a variable works
print("type of variable before ",type(myint))
myint = "abc"
print("redeclaring int variable", myint)
print("type of variable after ",type(myint))