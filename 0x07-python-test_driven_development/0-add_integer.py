#!/usr/bin/python3
""" 
This is a function it does
a different tests with the use 
edge cases.
"""


def add_integer(a, b=98):
    """ this is a function that
    return an add with two integers
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    
    return a + b

