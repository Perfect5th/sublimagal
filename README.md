# Sublimagal

## Embed ASCII Text in PNG Images

This is a Python utility for secreting text in the least-significant bits of PNG files. It works by encoding the length of the message and the message itself in the last bit of the red channel of each pixel, sequentially from the top left pixel of the image in horizontal scan lines.

Currently the only dependency is [Pillow](https://python-pillow.org/)

Future plans are:

  * use all four (r, g, b, a) channels, as the current maximum message size is ((w * h) / 8) - 16 bytes.
  * make into a bash-usable command
  * package on pypi
  
Current usage requirements:

  * Python 3.7
  * pipenv
  
Current usage:

```
$ git clone https://github.com/Perfect5th/sublimagal.git
$ cd sublimagal

$ pipenv shell

# To encode a message into a PNG
$ ./main.py -i inputfile.png -o outputfile.png "This is a secret message"

# To decode a message from a PNG
$ ./decode.py outputfile.png
This is a secret message
```
