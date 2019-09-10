#!/usr/bin/env python3

from PIL import Image


def get_bytes(bits):
    done = False

    while not done:
        byte = 0

        for _ in range(8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True

            byte = (byte << 1) | bit

        yield byte


if __name__ == '__main__':
    input_image = Image.open('testoutput.png')

    input_pixels = input_image.load()

    as_bits = []

    size_x = 0
    size_y = 0
    for i in range(16):
        pixel = input_pixels[size_x, size_y]
        rgb = pixel[0]

        as_bits.append(rgb % 2)

        size_x = (size_x + 1) % input_image.width

        if size_x == 0:
            size_y = (size_y + 1) % input_image.height

            if size_y == 0:
                raise Exception("Image not large enough for embedding")

    itr = get_bytes(iter(as_bits))
    byte1 = next(itr)
    byte2 = next(itr)
    message_size = (byte1 << 8) + byte2

    as_bits = []

    for y in range(size_y, input_image.height):
        for x in range(size_x, input_image.width):
            pixel = input_pixels[x, y]
            rgb = pixel[0]

            as_bits.append(rgb % 2)

            if len(as_bits) >= message_size * 8:
                break

        break

    counter = 0
    message = ''
    for b in get_bytes(iter(as_bits)):
        message += chr(b)

    print(message)
