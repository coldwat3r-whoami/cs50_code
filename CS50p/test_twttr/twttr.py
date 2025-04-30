def main():
    # Request user input
    word = input("Input: ")
    # convert the provided text with function
    print(shorten(word))


def shorten(word):
    # Needs a list of characters to exclude
    chrctrs = [
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"
    ]

    # Needs to iterate through provided phrase looking for characters in exclude list
    for c in chrctrs:
        # Needs to replace exclude list character found in phrase with nothing
        if c in word:
            word = word.replace(c, "")
    # returns new phrase
    return f"Output: {word}"


if __name__ == "__main__":
    main()
