#!/usr/bin/python3

"""
a function that returns the number
of lines of a text file:
"""


def number_of_lines(filename=""):
    """ Return a number of lines """
    i = 0
    with open(filename, "r") as f:
        for line in f:
            i = i + 1
    return i
