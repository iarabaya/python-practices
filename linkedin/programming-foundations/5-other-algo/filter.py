# use a hashtable to filter out duplicate items

# define a set of items that we want to reduce duplicates
items = [ "apple", "pear", "orange", "banana", "apple",
    "orange", "apple", "pear", "banana", "orange",
    "apple", "kiwi", "pear", "apple","orange" ]

# TODO: create a hashtable to perform filter
filter = dict()

# TODO: loop over each item and add to the hashtable
for key in items:
  print(filter)
  filter[key] = 0

# TODO: create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(filter)
print(result)