from pyfiglet import Figlet
import sys, random


def random_font():
    text = input("Input: ")
    figlet = Figlet()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(text))


def user_font(f):
    figlet = Figlet()
    if f in figlet.getFonts():
        text = input("Input: ")
        figlet.setFont(font=f)
        print(figlet.renderText(text))
    else:
        sys.exit("No such font.")


def main():
    if len(sys.argv) == 1:
        random_font()
    elif len(sys.argv) == 3:
        if (
            sys.argv[1] == '-f' or
            sys.argv[1] == '--font'
):
            f = sys.argv[2]
            user_font(f)
        else:
            sys.exit("Wrong cli arguments")
    else:
        sys.exit("Wrong cli arguments")


if __name__ == '__main__':
    main()
