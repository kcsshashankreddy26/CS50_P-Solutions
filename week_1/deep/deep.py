name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if(name.strip() == "42"):
    print("Yes")
elif name.lower().strip() == "forty-two":
    print("Yes")
elif name.lower().strip() == "forty two":
    print("Yes")


else:
    print("No")
