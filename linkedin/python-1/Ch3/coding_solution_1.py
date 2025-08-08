def find_largest(test_strings):
  maxlen = 0
  for s in test_strings:
    if len(s) > maxlen:
      maxlen = len(s)
  return maxlen