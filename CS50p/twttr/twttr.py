def main():

    # Request user input
    phrase = input("Input: ")

    # convert the provided text with function
    cnvrtd = convert(phrase)
    print(f"Output: {cnvrtd}")


def convert(phrase):

    # Needs a list of characters to exclude
    chrctrs = [
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"
    ]

    # Needs to iterate through provided phrase looking for characters in exclude list
    for c in chrctrs:

        # Needs to replace exclude list character found in phrase with nothing
        if c in phrase:
            phrase = phrase.replace(c, "")

    # returns new phrase
    return phrase


main()
