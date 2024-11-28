def main():
    menu =[
            {"name":"Baja Taco","cost": 4.25},
            {"name":"Burrito","cost": 7.50},
            {"name":"Bowl", "cost" : 8.50},
            {"name":"Nachos","cost" : 11.00},
            {"name":"Quesadilla","cost" : 8.50},
            {"name":"Super Burrito", "cost" : 8.50},
            {"name":"Super Quesadilla","cost" : 9.50},
            {"name":"Taco","cost" : 3.00},
            {"name":"Tortilla Salad", "cost" : 8.00}
            ]

    try:
        total = 0
        while True:
            order = input("Place Your Order: ").title()
            for item in menu:
                if order == item["name"]:
                    total+= float(item["cost"])
                    answer = format(total,".2f")
                    print(f"Total: ${answer}")
    except EOFError:
        print()


main()