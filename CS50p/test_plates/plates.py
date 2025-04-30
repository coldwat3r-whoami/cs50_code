def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 6 >= len(s) >= 2:
        # Need to iterate through user input
        n = 0
        p = (len(s) - 1)
        new_plate = []

        # Need to make sure first two characters are letters
        while n < 2:
            if s[n].isalpha() and not s[n].isdigit():
                new_plate.append(s[n])
                n += 1
            else:
                return False

        # Need to make sure plate doesn't have 0 in the third position
        while p >= n >= 2:
            if s[n].isdigit() and s[n] != "0":
                new_plate.append(s[n])
                n += 1

            # Need to make sure it doesn't have letters after numbers
            elif s[n].isalpha() and not s[(n-1)].isdigit():
                new_plate.append(s[n])
                n += 1

            # need to allow 0 after initial number
            elif s[n].isdigit() and s[n] == "0" and s[(n-1)].isdigit():
                new_plate.append(s[n])
                n += 1

            else:
                return False

    # if all these statments are satisfied
        return True

    # can't be shorter than 2 or longer than 6
    else:
        return False


if __name__ == "__main__":
    main()

