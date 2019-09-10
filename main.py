#!/usr/bin/env python3

import argparse

from PIL import Image


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Embed a message in a PNG.')
    parser.add_argument(
        'message', nargs=1, type=str, help='The message to embed')
    parser.add_argument(
        '-i', '--input', nargs=1, type=str,
        help='The image in which to embed the message')
    parser.add_argument(
        '-o', '--output', nargs=1, type=str,
        help='The destination output file')

    args = parser.parse_args()

    output_image = Image.open(args.input[0])

    output_pixels = output_image.load()

    input_message = args.message[0]
    input_size = len(input_message)
    x = 0
    y = 0

    # Encode first two bytes as message length
    as_bits = []

    for j in range(16):
        bit = input_size >> j
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

    for input_byte in bytes(input_message, 'ascii'):
        as_bits = []

        for i in range(8):
            bit = input_byte >> i
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

    output_image.save(args.output[0], compress_level=0)
