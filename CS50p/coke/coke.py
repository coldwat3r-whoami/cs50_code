def main():

    print("Amount Due: 50")

    # Request input
    coins = int(input("Insert Coin: "))

    # Restricted to only valid coin values
    if coins == 25 or coins == 10 or coins == 5:
        change_needed = needs_change(coins)

    # If provided invalid coin value, prompt again
    else:
        main()


def needs_change(coins):

    amount_due = 50

    # Needs to keep prompting if less than amount due
    if coins < amount_due:
        more_coin = amount_due - coins
        print(f"Amount Due: {more_coin}")
        coins = coins + int(input("Insert Coin: "))
        needs_change(coins)

    # Needs to know when change is owed
    elif coins > amount_due:
        change_owed = coins - amount_due
        print(f"Change Owed: {change_owed}")

    # Needs to stop if amount is provided
    elif coins == amount_due:
        print("Change Owed: 0")


main()
