'''
"99 Bottles of Beer" is a traditional song in the United States and Canada.
It is popular to sing on long trips, as it has a very repetitive format which is
easy to memorize, and can take a long time to sing. The song's simple lyrics are
as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is
completed when the singer or singers reach zero.
Your task here is write a Python program capable of generating all the verses
of the song.
'''

def beer():
    n = 99
    song = ""

    while n > 1:
        song += """{} bottles of beer on the wall, {} bottles of beer.\n\
Take one down, pass it around, {} {} of beer on the wall.\n\n""".\
        format(n, n, n-1, "bottles" if n-1 > 1 else "bottle")
        n -= 1
    song += """1 bottle of beer on the wall, 1 bottle of beer.\n\
Take one down and pass it around, no more bottles of beer on the wall.\n\n\
No more bottles of beer on the wall, no more bottles of beer.\n\
Go to the store and buy some more, 99 bottles of beer on the wall."""

    return song

def main():
    song = beer()

    return print(song)

if __name__ == '__main__':
    main()
