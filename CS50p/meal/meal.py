def main():
    time = input("What time is it? ").strip(" ")
    formatted = convert(time)

    if 7 <= formatted <= 8:
        print("breakfast time")
    elif 12 <= formatted <= 13:
        print("lunch time")
    elif 18 <= formatted <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    numbers = float(minutes) / 60
    newtime = float(hours)+numbers
    return newtime


if __name__ == "__main__":
    main()
