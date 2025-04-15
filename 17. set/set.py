utensils = {"fork", "spoon", "knife","knife"}
dishes = {"bowl", "plate", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update({"plate", "cup", "bowl"})
utensils.update(dishes)
dinner_table = utensils.union(dishes)

print(dinner_table)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)
