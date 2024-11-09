#!/usr/bin/python3
"""using sys module to check number of arguments
passed and to exit the code"""


import sys
import os.path


if __name__ == "__main__":
    """changing markdown to html"""

    if len(sys.argv) < 3:
        print(
                'Usage: ./markdown2html.py README.md README.html',
                file=sys.stderr
                )
        sys.exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not os.path.isfile(inputFile):
        print(f'Missing {inputFile}', file=sys.stderr)
        sys.exit(1)

    else:
        sys.exit(0)
