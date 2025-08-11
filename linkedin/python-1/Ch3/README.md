# Code challenge Ch3.1
# Find the longest string in a list of strings
You're given a list of strings.

Your task: Return the length of the longest string in the list.

## Parameters
the_strings: A list of strings

## Result
int: The length of the longest string in the list

### Example 1:
Input: ["Hello", "World", "This is a string"]
Result: 16

# Code challenge Ch 3.2
# Determine whether a string is a palindrome
Your function is given a string as a parameter.
Your task: Return a Boolean True or False value, indicating whether the string is a palindrome. A palindrome is a string that reads the same forward and backward, ignoring spaces, capitalizacion and punctuation.
Example palindromes: "Radar", "Race car", and "Madam, I'm Adam"
"Radar" is the same both backward and forward, ignoring letter casing.
"Race car!" is also the same both ways, ignoring case and punctuation and removing the space.
"Madam, I'm Adam" is the same when all punctuation, spaces and casing are removed.

## Parameters
testst: A string

## Result
Boolean: True or False depending on whether the string is a palindrome

## Constraints
The teststr parameter is always at least one character long

### Example 1:
Input: "Hello World!"
Result: False

### Example 2:
Input: "Radar"
Result: True