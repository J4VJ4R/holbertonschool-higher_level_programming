#!/usr/bin/python3

"""
module for write_file
"""


def write_file(filename="", text=""):
    """ Return a number of characters """
    with open(filename, "w") as file:
        count = file.write(text)
    return count
