#!/usr/bin/env python3

from PIL import Image


if __name__ == '__main__':
    output_image = Image.open('testinput.png')

    output_pixels = output_image.load()

    input_file = open('testinput.txt', 'rb')
    input_byte = input_file.read(1)
    x = 0
    y = 0

    while input_byte:
        as_bits = []

        for i in range(8):
            bit = int.from_bytes(input_byte, 'big') >> i
            as_bits.append(bit % 2)

        while as_bits:
            bit = as_bits.pop()
            pixel = output_pixels[x, y]
            rgb = pixel[0]

            if bit and rgb % 2 == 0:
                rgb += 1
            elif not bit and rgb % 2 == 1:
                rgb -= 1

            output_pixels[x, y] = (rgb, pixel[1], pixel[2])

            x = (x + 1) % output_image.width

            if x == 0:
                y = (y + 1) % output_image.height

                if y == 0:
                    raise Exception("Image not large enough for embedding")

        input_byte = input_file.read(1)

    output_image.save('testoutput.png', compress_level=0)
