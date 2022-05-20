#!/usr/bin/env python3
"""
Bionic text - emphasise the first few letters to make speed reading easier.
Whipped up in 20 minutes to play around with the idea in Markdown

Arguments:
    py bionic-reading.py in out


    in: the input file
    out: the output file, with each first half pre- and post-pended with "**" by default.

Usage:
    py bionic-reading.py in.md out.md
"""

__author__ = "Mikanwolfe"
__version__ = "0.1.0"
__license__ = "MIT"

pre = "**"
post = "**"

import argparse

def main(args):
    """ Main entry point of the app """
    with open(args.readFrom) as f:
        lines = f.readlines()

    write = open(args.writeTo, "w+")
    for row in lines:
        bionicWords = []
        words = row.split()
        for word in words:
            if len(word) != 1:
                if word.find('#') == -1 or word.find('*') == -1:
                    half = round(len(word)/2)
                    bionicWord = pre + word[0:half] + post + word[half:len(word)]
                    bionicWords.append(bionicWord)
            else:
                bionicWords.append(word)
        
        bionicRow = ' '.join(bionicWords)


        write.write(bionicRow + "\n")
        print(bionicRow)

    write.close()

    





if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("readFrom", help="File to read from")
    parser.add_argument("writeTo", help="File to write to")

    args = parser.parse_args()
    main(args)
