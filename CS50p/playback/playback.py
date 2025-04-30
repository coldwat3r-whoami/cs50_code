import re


def main():

    user_input = input("Please type here: ")
    slow_text = re.sub(" ", "...", user_input)
    print(slow_text)


main()
