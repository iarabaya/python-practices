
def count_numbers(which, numbers):
  if which != "even" and which != "odd":
    return -1
  
  result = 0
  for num in numbers:
    if which == "even" and num % 2 == 0:
      result += 1
    if which == "odd" and num % 2 != 0:
      result += 1
  return result