#amount_due = 50

#while amount_due > 0:
#    print("Amount Due: ",amount_due)
 #   coin = int(input("Insert Coin: "))
#
 #   if coin in [25,10,5]:
  #      amount_due -= coin
#
#change_owed = abs(amount_due)
#print("Change Owed: ",change_owed)
amount_due = 50

while amount_due > 0:
    # Print the current amount due before prompting for a coin
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin  # Update amount_due after accepting valid coin

change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")