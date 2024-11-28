months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    user_input = input("Date: ").strip()
    try:
        if user_input[0].isnumeric():
            result = direct_convert(user_input)
            print(result)
        elif user_input[0].isalpha():
            result = month_convert(user_input)
            return result
    except:
        pass
        main()

def direct_convert(user_input):
    updated_data = user_input.split("/")
    if int(updated_data[1]) <= 31 and int(updated_data[0]) <=12:
        result = f"{updated_data[2]}-{str(updated_data[0]).zfill(2)}-{str(updated_data[1]).zfill(2)}"
        return result
    else:
        raise Exception("Invalid Format for Numeric value input")

def month_convert(user_input):
    updated_data = user_input.split(" ")
    if updated_data[0].title() in months and int(updated_data[1]).endswith(",") and int(updated_data[1][:-1])<31:
        month = months.index(updated_data[0].title())+1
        result = f"{updated_data[2]}-{str(month).zfill(2)}-{(updated_data[1][:-1]).zfill(2)}"
        return result
    else:
        raise Exception("Invalid Format for Month")



if __name__ == "__main__":
    main()