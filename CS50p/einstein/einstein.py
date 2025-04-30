def albert(phrase):

    c = 300000000
    E = phrase * (c**2)
    return E

def main():

    mass = int(input("Enter mass: "))
    solved = albert(mass)
    print(solved)

main()
