# The Merge Sort Algorithm
# Divide-and-conquer algorithm
# Breaks a dataset into individual pieces and merges them
# Uses recursion to operate on datasets
# Performs well on large sets of data
# In general has a performance of O(n log n) time complexity (log linear)

# implement a merge sort with recursion

items = [6,20, 8, 19, 56, 23, 87, 49, 41, 53]

def mergessort(dataset):
  if len(dataset)>1:
    mid = len(dataset) // 2
    leftarr = dataset[:mid] #split en python
    rightarr = dataset[mid:]

    # TODO: recursively break down the arrays
    mergessort(leftarr)
    mergessort(rightarr)

    # TODO: now perform the merging
    i=0 # index into the left array
    j=0 # index into the right array
    k=0 # index into merged array

    # TODO: while both arrays have content
    while i < len(leftarr) and j < len(rightarr):
      if leftarr[i] < rightarr[j]:
        dataset[k] = leftarr[i]
        i += 1
      else:
        dataset[k] = rightarr[j]
        j += 1
      k += 1

    # TODO: if the left array still has values, add them
    while i < len(leftarr):
      dataset[k] = leftarr[i]
      i += 1
      k += 1

    # TODO: if the right array still has values, add them
    while j < len(rightarr):
      dataset[k] = rightarr[j]
      j += 1
      k += 1

# test the merge sort with data
print(items)
mergessort(items)
print(items)