def main():

    # needs to take user input
    fraction = input("Fraction: ")
    print(percentage(fraction))


def percentage(f):

    p = f.split('/')

    try:
        # convert to int, if not then raise exception
        x = int(p[0])
        y = int(p[1])

        # x cant be greater than y
        # lexicographic comparison means 9 > 1 (ex. 99 > 100)
        if x > y:
            main()
        else:
            calc = round((x / y) * 100)

    # y cannot be 0, reprompt user
    except ZeroDivisionError:
        main()
    # x and y must be int, reprompt user
    except ValueError:
        main()

    # can't be greater than 100%
    if calc > 100:
        main()
    # need to specify F and E amounts
    elif calc > 98:
        return ("F")

    elif calc < 2:
        return ("E")

    else:
        return (f"{calc}" + "%")


main()

