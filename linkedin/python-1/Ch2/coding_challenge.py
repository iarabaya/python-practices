show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
  even_counter = 0
  odd_counter = 0
  if which != "even" and which != "odd":
    return -1
  
  for num in numbers:
    if num % 2 == 0:
      even_counter = even_counter + 1
    else: 
      odd_counter = odd_counter + 1
  
  if which == "even":
    return even_counter
  elif which == "odd":
    return odd_counter