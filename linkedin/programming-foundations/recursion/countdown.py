# Recursion
# Is when a function calls itself within
# Recursive funcions need to have a breaking condition (avoid infinite loops)
# This prevents infinite loops and eventual crashes
# Each time the function is called, the old arguments are saved
# This is called the "call stack"

# use recursion to implement a countdown counter
def countdown(x):
  if (x == 0):
   print("done!")
   return
  else:
    print(x, "...")
    countdown(x-1)
    print("foo", x) # executes after the countdown is complete

countdown(4) 