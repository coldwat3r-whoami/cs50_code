def menu_items(n):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    try:
        while True:
            if n in menu:
                total += menu.get(n)
                print(f'Total: ${total:.2f}')
                n = input("Item: ").title()
            else:
                n = input("Item: ").title()

    except EOFError:
        print("\n", end="")
        return


def main():
    try:
        menu_items(input("Item: ").title())
    except:
        print("\n", end="")
        return


main()
