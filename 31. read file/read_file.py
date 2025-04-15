try:
    with open("/Users/dimitarmitev/Desktop/python-course/31. read file/test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")