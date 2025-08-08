# Count the number of even or odd numbers in a list

You're given a list of integers and a string indicating what kind of numbers to count.
Your task: Count the number of even or odd numbers in the list, based upon the string argument.

## Parameters
which: A string indicating what kind of numbers to count
numbers: A list of integers

## Result
int: The count of the type of numbers in the list (even or odd)

## Constraints
The numbers list always contains at least one number.
All numbers in the list will be >=0.
The string argument can be anything, so your code needs to check for "even" or "odd" (in lowercase).
If the which argument is not "even" or "odd", return -1.

### Example 1:
Input: "even", [2,5,20,30,55]
Result: 3

### Example 2:
Input: "blarg", [20,30,55]
Result: -1
