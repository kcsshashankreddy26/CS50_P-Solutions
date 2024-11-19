def main():
    answer = input("what's the time?: ")
    time = convert(answer)

    #breakfast time
    if time >= 7 and time <= 8:
        print("Breakfast Time")
    #lunch time
    if time >= 12 and time <= 13:
        print("Lunch Time")
    #dinner time
    if time >= 18 and time <= 19:
        print("Dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes)/60

    return float(hours) + new_minute


if __name__ == "__main__":
    main()