def main():
    user_input = input("Fraction: ").strip()
    answer = check_input(user_input)
    if answer > 100:
        main()
    elif answer >= 99:
        print("F")
    elif answer <= 1:
        print("E")
    else:
        print(f"{answer}%")
def check_input(user_input):
    while True:
        try:
            numerator,denominator = user_input.split("/")
            percentile = round((int(numerator) / int(denominator))*100)
            return int(percentile)
        except(ValueError , ZeroDivisionError , IndexError):
            pass

main()
