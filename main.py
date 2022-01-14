import os
from PIL import Image


path = os.path.abspath('images')

def main():
    images_path = [os.path.join(path, image) for image in os.listdir(path)]

    for image_path in images_path:
        image = Image.open(image_path)
        width, height = image.size
        new_width, new_height = 2 * width, 2 * height
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image.save(image_path, format="jpeg")


if __name__ == '__main__':
    main()

