import inflect
p = inflect.engine()
list_names = [ ]# empty list to store names
while True:
    #gets the input from the user until the user press ctrl-d
    try:
        usr_input = input("Name: ")
        list_names.append(usr_input)

    except EOFError:#to exit the loop when the user press ctrl-d
        print()
        break
#list_names = p.join(list_names)
#print(f"Adieu, adieu, to {list_names}")
# or the code below can be used
print(f"Adieu, adieu, to {p.join(list_names)}")
