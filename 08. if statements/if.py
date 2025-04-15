age = input("How old are you?: ")

if age >= "18":
    print("You are an adult")
elif age == "100":
    print("You are a century old")
elif age >= "13":
    print("You are a teenager")
elif age <= "0":
    print("You haven't been born yet")
else:
    print("You are a kid")