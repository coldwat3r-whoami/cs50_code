import csv
import sys


def convert(file):
    fixed_file = []
    for row in file:
        last_name, first_name = row.get("name").split(",")
        house = row.get("house")
        fixed_file.append({
            "first": first_name.strip(" "),
            "last": last_name,
            "house": house
        })
    return fixed_file


def output(file):
    with open(sys.argv[2], "w") as csv_file:
        keys = ["first", "last", "house"]
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        for row in file:
            writer.writerow(row)


def main():
    try:
        if len(sys.argv) < 3:
            raise Exception("Too few command-line arguments")
        elif len(sys.argv) > 3:
            raise Exception("Too many command-line arguments")
        else:
            with open(sys.argv[1]) as csv_file:
                file = csv.DictReader(csv_file)
                output(convert(file))
    except FileNotFoundError:
        raise Exception(f'Could not read {sys.argv[1]}')


if __name__ == "__main__":
    main()

