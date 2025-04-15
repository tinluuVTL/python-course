student = ("Dimitar", 32, "male")

print(student.count("Dimitar"))
print(student.index("male"))

for x in student:
    print(x)

if "Dimitar" in student:
    print("Dimitar is here!")