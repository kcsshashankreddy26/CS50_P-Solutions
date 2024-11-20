cC = input("camelCase: ")
print("snake_case: ", end = "")
for n in cC:
    if n.isupper():
        print("_" + n.lower(), end = "")
    else:
        print(n, end ="")