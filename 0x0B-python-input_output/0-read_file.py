#!/usr/bin/python3

"""
a function that reads a text file
(UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """ read a text """
    with open(filename, "r") as file:
        read_file = file.read()
    print(read_file, end="")
