#!/usr/bin/python3

"""
create a class rectangle and inherits
from Base
"""
from models.base import Base

class Rectangle(Base):
    """Private instance attributes"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ width of the rectangle """
        return self.__width    
       
     # a setter function 
    @width.setter 
    def width(self, w):
        """ set the widht """
        self.__width = w

    @property
    def height(self):
        """ height of the rectangle """
        return self.__height
       
     # a setter function 
    @height.setter
    def height(self, h):
        """ set the height """
        self.__height = h

    @property
    def x(self):
        """ x of the rectangle """
        return self.__x    
       
     # a setter function 
    @x.setter 
    def x(self, x):
        """ set the widht """
        self.__x = x

    @property
    def y(self):
        """ y of the rectangle """
        return self.__y  
       
     # a setter function 
    @y.setter 
    def y(self, y):
        """ set the widht """
        self.__y = y
