expression = input("Enter the Expression: ")

x, y, z = expression.split(" ")#splitting x,y,z as "x y z"

new_x = float(x)
new_z = float(z)
#assigning an operation to y variable
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z

#printing the result
print(result)