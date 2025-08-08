def find_largest(strings):
  string_lengths = []
  for s in strings:
    string_lengths.append(len(s))
  
  return max(string_lengths)