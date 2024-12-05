import random
import sys

def guessing(level):
        while True:
            random_choice = random.randint(1,level)
            while True:
                guess = int(input("Guess: ").strip())
                if guess < random_choice:
                    print("Too small!")

                elif guess > random_choice:
                    print("Too large!")

                elif guess == random_choice:
                    print("Just right!")
                    sys.exit()

def main():
    while True:
        try:
            while True:
                level = int(input("Level: ").strip())
                if level > 0:
                    guessing(level)
                    break
        except ValueError:
            pass
if __name__ == "__main__":
    main()