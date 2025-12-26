from PIL import Image


def main():
    try:
        im = Image.open('test image.jpg')
        width, height = im.size

        rgb_val = []

        for y in range(height):
            for x in range(width):
                # Get the RGB value of the pixel at (x, y)
                r, g, b = im.getpixel((x, y))
                rgb_val.append(((r+g+b)/3))

        print(rgb_val)

    except IOError:
        print('error')


if __name__ == '__main__':
    main()
