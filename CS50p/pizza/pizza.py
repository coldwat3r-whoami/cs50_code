import sys
import csv
from tabulate import tabulate


def convert(file):
    table = tabulate(file, headers="keys", tablefmt="grid")
    return table


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception("Too few command-line arguments")
        elif len(sys.argv) > 2:
            raise Exception("Too many command-line arguments")
        elif ".csv" not in sys.argv[1]:
            raise Exception("Not a CSV file")
        else:
            with open(sys.argv[1]) as csv_file:
                file = csv.DictReader(csv_file)
                print(convert(file))
    except (FileNotFoundError, ValueError, TypeError):
        raise Exception


if __name__ == "__main__":
    main()
