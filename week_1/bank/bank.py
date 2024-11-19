#get the input from the user
greet = input("Greeting: ").lower().strip()
#if greet with hello then $0
if "hello" in greet:
    print("$0")
#if greet starts with "h" other than hello then $20
elif greet[0]=="h":
    print("$20")
#if there is no greet then $100
else:
    print("$100")
