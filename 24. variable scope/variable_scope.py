name = "Ivan" # global scope

def display_name():
    name = "Dimitar" # local scope
    print(name)

display_name()
print(name)