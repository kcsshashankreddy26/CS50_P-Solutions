def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False


    if not s[0].isalpha() or not s[1].isalpha():
        return False


    for c in s:
        if not c.isalnum():
            return False


    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False
    return True

main()
