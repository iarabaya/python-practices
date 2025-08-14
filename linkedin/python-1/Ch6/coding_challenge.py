import os
from os import path

#example to read files
# try:
#   with open("textfile.txt", "r") as file:
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#   print("Error: 'textfile.txt' not found in the same directory")
# except Exception as e:
#   print(f"An error occurred: {e}")


def file_info():
  sizecount = 0
  if path.exists("deps") and path.isdir("deps"):
    with os.scandir("deps") as dir:
      for entry in dir:
        if entry.name.endswith(".txt") and entry.is_file():
          filesize = os.path.getsize(f"deps/{entry.name}")
          print(entry.name, filesize)
          sizecount += filesize
  else:
    print("Dir 'deps' does not extist")
  return sizecount

print("total:",file_info())