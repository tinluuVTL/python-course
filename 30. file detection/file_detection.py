import os

path = "/Users/dimitarmitev/Desktop/python-course/30. file detection/test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location does not exist!")