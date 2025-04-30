import random
import sys


def main():
    level = get_level()
    generate_integer(level)  # Start the quiz based on the selected level


def get_level():
    while True:  # Keep asking for a valid level until it's given
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level  # Return valid level and exit the loop
            else:
                print("Please enter a valid level (1, 2, or 3).")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")


def generate_integer(level):
    score = 0
    wrong_count = 0

    # Determine the number range based on the level
    if level == 1:
        min_num, max_num = 0, 9
    elif level == 2:
        min_num, max_num = 10, 99
    else:  # level == 3
        min_num, max_num = 100, 999

    # Main loop for 10 questions
    # Using "_" instead of "i" because we dont need the number
    for _ in range(10):
        first_num = random.randint(min_num, max_num)
        second_num = random.randint(min_num, max_num)

        # Loop until user gets the correct answer or wrong_count exceeds 3
        while True:
            try:
                answer = int(input(f"{first_num} + {second_num} = "))
            except ValueError:
                print("EEE")
                wrong_count += 1
                if wrong_count >= 3:
                    print(f"Score: {score}")
                    sys.exit()

            if first_num + second_num == answer:
                score += 1
                break  # Correct answer, move to the next problem
            else:
                print("EEE")
                wrong_count += 1
                if wrong_count >= 3:
                    print(f'{first_num} + {second_num} = {first_num + second_num}')
                    wrong_count = 0
                    break

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
