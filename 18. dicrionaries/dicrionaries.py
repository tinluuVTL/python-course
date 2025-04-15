capitals = {"USA":"Washington DC", "India":"New Dehli", "China":"Beijing", "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.pop("China")
capitals["USA"] = "Las Vegas"
# capitals.clear()

print(capitals["Russia"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)