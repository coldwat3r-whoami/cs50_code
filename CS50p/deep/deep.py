def main():

    question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    formatted = question.strip(" ").lower()
    if not (formatted == "42" or formatted == "forty-two" or formatted == "forty two"):
        print("No")
    else:
        print("Yes")

main()
