import emoji

def make_emoji(s):

    text = s.split()
    # This checks if there is additional user text
    if len(text) > 1:
        # This is to allow emoji in the beginning and end of input
        if len(text) > 2:
            first_emoji = emoji.emojize(text[0], language='alias')
            second_emoji = emoji.emojize(text[2], language='alias')
            print(f'Output: {first_emoji} {text[1]} {second_emoji}')
        else:
            second_emoji = emoji.emojize(text[1], language='alias')
            print(f'Output: {text[0]} {second_emoji}')
    # This assumes there is only emoji with no additional user text
    elif ':' in s:
            my_emoji = emoji.emojize(s, language='alias')
            print(f'Output: {my_emoji}')

    # Re-prompt if the user entered nothing
    else:
        main()



def main():
    user_string = input("Input: ")
    make_emoji(user_string)


if __name__ == '__main__':
    main()
