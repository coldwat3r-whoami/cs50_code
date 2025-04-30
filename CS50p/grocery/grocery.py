def groceries():
    grocery_list = {}
    while True:
        try:
            key = input()
            if key in grocery_list:
                grocery_list[key] += 1
            else:
                grocery_list[key] = 1
        except EOFError:
            for key in sorted(grocery_list):
                print(f'{grocery_list[key]} {key.upper()}')
            return


def main():
    groceries()


main()
