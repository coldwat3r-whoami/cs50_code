import requests
import sys


def main():
    if len(sys.argv) > 1:
        try:
            n = float(sys.argv[1])
        except Exception as err:
            print(err)
            sys.exit("Command-line argument is not a number")
        get_price(n)
    else:
        sys.exit("Missing command-line argument")


def get_price(n):

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = response.json()
        amount = price["bpi"]["USD"]["rate_float"]
        result = float(amount * n)
        print(f"${result:,.4f}")

    except requests.RequestException:
        print("Something went wrong...")


if __name__ == "__main__":
    main()
