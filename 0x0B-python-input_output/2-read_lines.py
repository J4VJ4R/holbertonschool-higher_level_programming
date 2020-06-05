#!/usr/bin/python3

"""
a function that reads n lines of a text file
(UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    """ Return a n number of lines of the text """
    i = len(open(filename).readlines())
    with open(filename, 'r') as file:
        if nb_lines > 0 and nb_lines < i:
            while nb_lines:
                print(file.read_line(), end="")
                nb_lines -= 1
        else:
            read_data = file.read()
            print(read_data, end="")
