def main():
    camel = input("camelCase: ")
    print(convert_snake(camel))

def convert_snake(camel):

    # Code needs to iterate through the input
    n = 0
    list = []
    while n < len(camel):
        list.append(camel[n])
        n += 1

    # It needs to add an underscore when it finds an uppercase
    i = 0
    while i < len(list):
        if list[i].isupper():
            list[i] = ('_'+ list[i])
            i += 1
        else:
            i += 1

    # Need to lowercase and join all items from list
    list = [x.lower() for x in list]
    list = "".join(list)

    # It needs to return the new phrase
    return list

main()
