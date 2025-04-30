import random
import sys


def compare_values(r):
    guess = int(input("Guess: "))
    if guess == r:
        print("Just right!")
        sys.exit()
    elif guess > r:
        print("Too large!")
        compare_values(r)
    elif guess < r:
        print("Too small!")
        compare_values(r)
    else:
        print("Something is not right...")


def main():
    try:
        level = int(input("Level: "))
        result = random.randint(1, level)
        compare_values(result)
    except Exception as err:
        print(err)
        main()


if __name__ == "__main__":
    main()
