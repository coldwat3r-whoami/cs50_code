import sys
import os
from PIL import Image, ImageOps

def combine_images(input_image, output_image):
    with Image.open(input_image) as img:
        shirt = Image.open("shirt.png")
        size = shirt.size
        ImageOps.fit(img, size)
        Image.Image.paste(img, shirt)
        img.save(output_image)
    return output_image


def main():
    extensions = [".jpg", ".jpeg", ".png"]
    try:

        if len(sys.argv) < 3:
            raise Exception("Too few command-line arguments")
        elif len(sys.argv) > 3:
            raise Exception("Too many command-line arguments")
        elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
            raise Exception("Input and output have different extensions")
        elif os.path.splitext(sys.argv[2])[1] not in extensions:
            raise Exception("Invalid output")
        else:
            sys.argv[2] = combine_images(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        raise Exception(f'Could not read {sys.argv[1]}')


if __name__ == "__main__":
    main()
