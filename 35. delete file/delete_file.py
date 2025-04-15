import os 
import shutil

path = "/Users/dimitarmitev/Desktop/python-course/35. delete file/test.txt"

try:
    # if os.path.exists(path):
    #     os.remove(path)
    #     print("File was deleted.")
    # else:
    #     print("That file was not found :(")
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path) # Delete a directory with all it's contents
except FileNotFoundError:
    print("That file was not found :(")
except PermissionError:
    print("You don't have permission to delete that :(")
except OSError:
    print("You can't delete that using that function :(")
else:
    print(path + " was deleted.")