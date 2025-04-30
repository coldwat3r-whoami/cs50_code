def convert(user_text):

    if ":" in user_text:
        convert_text = user_text.replace(":)", "🙂").replace(":(", "🙁")
        return convert_text

def main():

    text = input("Type here: ")
    converted = convert(text)
    print(converted)

main()
