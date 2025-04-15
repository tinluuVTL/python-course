animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {0} jumped over the {1}".format(animal, item))
print("The {} jumped over the {}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="horse", item="table"))

text= "The {animal} jumped over the {item}"
print(text.format(animal="horse", item="table"))

name="Dimitar"

print("Hello, ny name is {}".format(name))
print("Hello, ny name is {:10}. Nice to meet you.".format(name))
print("Hello, ny name is {:<10}. Nice to meet you.".format(name))
print("Hello, ny name is {:>10}. Nice to meet you.".format(name))
print("Hello, ny name is {:^10}. Nice to meet you.".format(name))

number = 10000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:e}".format(number))



