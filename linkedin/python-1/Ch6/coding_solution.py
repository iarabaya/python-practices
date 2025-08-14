import os
from os import path

def file_info():
  totalbytes = 0
  folder = "deps"
  # get a list of all the files in the current directory
  dirlist = os.listdir(folder)

  for entry in dirlist:
    # make sure it's a file
    if path.isfile(folder + "/" + entry) and entry.endswith(".txt"):
      # add the file size to the total
      filesize = path.getsize(folder + "/" + entry)
      print(entry, filesize)
      totalbytes += filesize

  return totalbytes

print("total:",file_info())