def is_palindrome(teststr):

  # newstr = [ char.upper() for char in teststr if char.isalpha()] #list comprehension
  # clean the string from special characters
  newstr = ""
  for char in teststr:
    if char.isalpha():
      newstr += char.upper()

  reversedstr = newstr[::-1]
  return newstr == reversedstr




print(is_palindrome("Radar"))
print(is_palindrome("RACE CAR!"))
print(is_palindrome("Hello World"))
print(is_palindrome("A man, a plan, a canal Panama!"))