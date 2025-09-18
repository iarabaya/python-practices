# The Quick Sort Algorithm
# Divide-and-conquer algorithm, like the merge sort
# Also uses recursion to perform sorting
# Generrally performs better than merge sort,O(n log n)
# Operates in place on the data
# Worst case is O(n2) when data is mostly sorted already

# Has pivot point selection
# Implement a quicksort

items = [20, 6, 8, 53, 56, 23, 87, 49, 41, 19]

def quicksort(dataset, first, last):
  if first < last:
    # calculate the split point
    pivotIndex = partition(dataset, first, last)

    # now sort the two partitions
    quicksort(dataset, first, pivotIndex - 1)
    quicksort(dataset, pivotIndex + 1, last)

def partition(datavalues, first, last):
  # choose the first item as the pivot value
  pivotValue = datavalues[first]
  # establish the upper and lower indexes
  lowerIndex = first + 1
  upperIndex = last

  # start searching for the crossing point
  done = False
  while not done:
    # TODO: advance the lower index
    while lowerIndex <= upperIndex and datavalues[lowerIndex] <= pivotValue:
      lowerIndex += 1

    # TODO: advance the upper index
    while datavalues[upperIndex] >= pivotValue and upperIndex >= lowerIndex:
      upperIndex -= 1

    # TODO: if the two indexes cross, we have found the split point
    if upperIndex < lowerIndex:
      done= True
    else:
      temp = datavalues[lowerIndex]
      datavalues[lowerIndex] = datavalues[upperIndex]
      datavalues[upperIndex] = temp
    pass

  # when the split point is found, exchange  the pivot value
  temp = datavalues[first]
  datavalues[first] = datavalues[upperIndex]
  datavalues[upperIndex] = temp

  # return the split point index
  return upperIndex

# test the merge sort with data
print(items)
quicksort(items, 0, len(items)-1)
print(items)
