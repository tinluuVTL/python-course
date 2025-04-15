import os 

source = "/Users/dimitarmitev/Desktop/python-course/34. move file/test.txt"
destination = "/Users/dimitarmitev/Desktop/copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved.")
except FileNotFoundError:
    print(source + " was not found.")