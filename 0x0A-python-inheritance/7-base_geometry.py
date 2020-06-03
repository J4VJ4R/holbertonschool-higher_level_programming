#!/usr/bin/python3

"""
an empty class BaseGeometry
"""


class BaseGeometry:
    """ Class BassGeomtery """
    pass

    def area(self):
        """ Here an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
