def add(*stuff):
    sum = 0;
    stuff = list(stuff)
    stuff[0] = 0
    for n in stuff:
        sum += n
    return sum

print(add(5, 5, 3,6,8,12,4))