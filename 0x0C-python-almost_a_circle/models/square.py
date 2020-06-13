#!/usr/bin/python3

"""
Write the class Square that inherits from Rectangle:
"""


from models.rectangle import Rectangle


class square(Rectangle):
    """ This is the class square """
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__( x, y, )
        return "[{}] ({}) {}/{} - {}".format("Square", )