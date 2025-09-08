# Stack collection that supports push and pop operations
# The last item pushed is the first one popped (LIFO)
# Practical applications: expression processing, backtracking: browser back stack

stack = []

# push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop an item off the stack
x = stack.pop()
print(x)
print(stack)