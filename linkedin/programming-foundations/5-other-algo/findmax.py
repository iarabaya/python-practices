# use a recursive algorithm to find a maximum value

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(itemList):
  # TODO: breaking condition: last item in list? return it
  if len(itemList) == 1:
    return itemList[0]
  
  # TODO: otherwise get the first item and call function
  # again to operate on the rest of the list
  op1 = itemList[0]
  print("primer item: ", op1)
  op2 = find_max(itemList[1:])
  print(op2)
  # TODO: perform the comparison when we're down t just two
  if op1 > op2:
    return op1
  else:
    return op2


# test the function
print(items)
print(find_max(items))
