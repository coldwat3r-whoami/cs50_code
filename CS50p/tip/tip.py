def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    mealPrice = float(d.replace("$", ""))
    return mealPrice

def percent_to_float(p):
    fixPercent = float(p.replace("%", ""))
    percentage = fixPercent / 100
    return percentage

main()
