#!/usr/bin/python3

"""
this is a first class
"""


class Base:
    """ class base for the other objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """ return id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
