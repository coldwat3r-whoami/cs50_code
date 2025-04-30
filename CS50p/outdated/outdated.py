def convert_written(date):
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    if ',' not in date[1]:
        main()
    else:
        try:
            day = date[1].replace(',', '')
            day = int(day)  # Convert day to integer to validate later
        except:
            main()

    month_name = date[0]
    year = date[2]

    if month_name in months and not day > 31:
        month = months.index(month_name) + 1  # Get month index (1-based)
        print(f'{year}-{month:02}-{day:02}')
    else:
        main()

def convert_numerical(date):
    try:
        # Convert to integers for validation
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        if not month > 12 and not day > 31:
            print(f'{year}-{month:02}-{day:02}')
        else:
            main()
    except:
        main()

def main():
    date_input = input("Enter date: ").strip()

    if '/' in date_input:
        # Numerical format: MM/DD/YYYY
        num_date = date_input.split('/')
        convert_numerical(num_date)

    # Otherwise, handle written date format like "September 8, 1999"
    else:
        new_date = date_input.split()

        # The date should have exactly 3 parts: month, day, year
        if len(new_date) == 3:
            convert_written(new_date)
        else:
            main()


if __name__ == "__main__":
    main()
