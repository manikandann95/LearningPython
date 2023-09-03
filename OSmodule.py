import os
os.write("novel.txt")
#consider novel, first_draft exists in folder of this py file saved already.
os.remove("novel.txt") # FileNotFound Error will come, if file doesn't exist
os.rename("first_draft.txt,final_masterpiece.txt") #rename(old_name, new_name)
os.path.exists("final_masterpiece.txt") # Output: True
os.path.exists("novel.txt") # Output: False

os.path.getsize("final_masterpiece.txt") # Size eg:142 characters

import datetime from datetime

mtime = os.path.getmtime("final_masterpiece.txt") # Output: 1242525626.143 Unix Timestamp (seconds from Jan 1, 1970) still using databases, unix programs 
# To convert it
datetime.fromtimestamp(mtime)

import os
file= "file.dat" # Not creating any file
if os.path.isfile(file): # If file.dat doesn't exist, returns False
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")

os.path.abspath("final_masterpiece.txt") # Output: /home/manik/final_masterpiece.txt
os.getcwd() # Current Directory cwd
os.mkdir("Python_examples") # Make Directory
os.chdir("Python_examples") # Change cwd to this one : /home/manik/Python_examples
os.getcwd()

os.mkdir("new_dir")
os.rmdir("new_dir") # Only removes empty directory

os.listdir("Python_examples") # Output: Produces List with all dir, file names
# ['images', 'file1.txt', 'file2.py']
os.path.isdir("images") # True

dir = "Python_examples"
for name in os.listdir(dir):
  fullname = os.path.join(dir, name)
  # os.path.join we can concatenate directories in a way that can be used with other os.path() functions.
  print(fullname) # Python_examples/images
