import inflect


def sound_of_music(song):
    # Create an inflect engine
    p = inflect.engine()

    # If there is only one name
    if len(song) == 1:
        print(f'\nAdieu, adieu, to {song[0]}')

    # If there are exactly two names
    elif len(song) == 2:
        print(f"\nAdieu, adieu, to {p.join(song[0:2])}")

    # If there are three or more names
    else:
        print(f'\nAdieu, adieu, to {p.join(song)}')


def main():
    song = []
    try:
        while True:
            song.append(input("Name: "))
    except EOFError:
        sound_of_music(song)


if __name__ == '__main__':
    main()
