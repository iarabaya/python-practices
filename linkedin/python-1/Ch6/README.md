# Count the size in bytex of text files in a directory
There is a set of files in the "deps" directory, which is a the same directory level that your code is running in. There are no subdirectories within this "deps" folder.
Your task: Calculate and return the total size in bytes of the text files within the "deps" directory. Only include text files that end with ".txt" in your calculation. Other files should be ignored.

## Parameters
No parameters are passed to your function.

## Result
int: Total byte count of all the text files in the directory

## Want a hint?
Check out the os and os.path modules in Python standard library. Your code will need to:
List the contents of the "deps" folder.
Iterate over each file and determine the size of each file if it is a ".txt file".
Add the size of the total byte count if it is a text file.
Return the total bytes