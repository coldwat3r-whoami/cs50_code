def main():

    x = input("Expression: ").replace(" ", "")
    y = float(eval(x))
    print(round(y, 1))

main()
