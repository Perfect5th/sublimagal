# Sublimigal

## Embed ASCII Text in PNG Images Like, Super Easily

Alright, listen up – I may have had a bit to drink, but I made this thing 
after I had an idea (probably while also drinking).

Let's hide secret messages inside PNG files without telling anyone (shhhhh).

TODO: Make this a CLI thingy

Get yourself set up, fool:

```
$ git clone <whatever the repo is called>
$ cd <into that>

$ pipenv shell

# To encode a cool message that you want your friends (??) to read:
$ ./main.py -i inputfile.png -o outputfile.png "This is my secret, motherfucker"

# To decode a cool message that your totally real friend made:
$ ./decode.py outputfile.png
This is my secret, motherfucker
```

Enjoy yourself and please remind me to update this README when I am sober 
before a potential employer sees it.
