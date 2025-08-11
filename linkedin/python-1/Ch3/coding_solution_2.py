def is_palindrome(teststr):
# convert the string to all lowercase
  temp = teststr.lower()

# strip all the spaces and punctuation from the string
  newstr = ""
  for c in temp:
    if c.isalnum():
      newstr += c

# now calculate the reverse of the string
  reversestr = ""
  strindx = len(newstr)-1
  while (strindx >= 0):
    reversestr += newstr[strindx]
    strindx -= 1

  if newstr == reversestr:
    return True
  return False




print(is_palindrome("Radar"))
print(is_palindrome("RACE CAR!"))
print(is_palindrome("Hello World"))
print(is_palindrome("A man, a plan, a canal Panama!"))