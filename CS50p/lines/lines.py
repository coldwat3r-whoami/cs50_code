import sys


def function():
    line_count = 0
    try:
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            for line in data:
                line = line.lstrip(" ")
                if not line.startswith("\n") and not line.startswith("#"):
                    line_count += 1
                else:
                    pass
    except Exception as e:
        print(f'Unexpected error raised: {e}')
    return line_count


def main():
    if not sys.argv[1]:
        raise Exception("Too few command-line arguments")
    elif len(sys.argv) > 2:
        raise Exception("Too many command-line arguments")
    elif sys.argv[1] is None:
        raise FileNotFoundError("File does not exist")
    if ".py" not in sys.argv[1]:
        raise Exception("Not a Python file")
    else:
        print(function())


if __name__ == "__main__":
    main()
