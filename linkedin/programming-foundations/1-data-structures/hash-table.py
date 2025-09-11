# Key-to-value mappings are unique
# Hash tables are typically very fast
# For small datasets, arrays are usually more efficient
# Hash tables don't order entries in a predictable way

# create a hashtable all at once
items1 = dict({ "key1": 1, "key2": 2, "key3": "three"})
print(items1)

# create a hashtable progressively
items2 = dict({})
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# try to access a nonexisten key
# print(items1["key6"])

# replace an item
items2["key2"]= "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items():
  print("Key: ", key, " value: ", value)