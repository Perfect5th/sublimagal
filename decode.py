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

    for y in range(input_image.height):
        for x in range(input_image.width):
            pixel = input_pixels[x, y]
            rgb = pixel[0]

            as_bits.append(rgb % 2)

    counter = 0
    for b in get_bytes(iter(as_bits)):
        print(chr(b))
        counter += 1
        if counter > 25:
            break
