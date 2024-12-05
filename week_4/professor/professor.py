import random

def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
         x = random.randint(100,999)
         y = random.randint(100,999)
    return x,y


def game(level):
    problem_count = 1
    score = 0
    while problem_count<=10:
        x,y = generate_integer(level)
        select_level = game_working(x,y)
        if select_level == True:
            score+=1
        problem_count +=1
    return score

def game_working(x,y):
    count = 1
    while count <=3:
        try:
            answer = int(input(f"{x} + {y} =  "))
            if answer == (x + y):
                return True
            else:
                count+=1
                print("EEE")
        except ValueError:
            count+=1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


if __name__ == "__main__":
    main()