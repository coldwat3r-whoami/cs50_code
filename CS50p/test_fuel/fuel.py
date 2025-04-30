def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ZeroDivisionError, ValueError):
        main()


def convert(fraction):
    p = fraction.split('/')

    try:
        x = int(p[0])
        y = int(p[1])

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

        return round((x / y) * 100)

    except ValueError:
        raise ValueError

def gauge(percentage):
    if percentage > 100:
        raise ValueError
    if percentage > 98:
        return "F"
    elif percentage < 2:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
