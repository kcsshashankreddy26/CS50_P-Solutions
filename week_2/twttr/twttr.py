name = input("Enter the text :  ")
print("Output: " , end = "")
for i in name:
    if i =="a" or i =="e" or i =="i" or i == "o" or i == "u" or i =="A" or i =="E" or i =="I" or i =="O" or i =="U":
        print("", end = "")
    else:
        print(i , end = "")

print()
