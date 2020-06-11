#!/usr/bin/python3

"""
create a class rectangle and inherits
from Base
"""


from models.base import Base


class Rectangle(Base):
    """Private instance attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        i = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of the rectangle """
        return self.__width

    @width.setter
    def width(self, w):
        """ set the widht """
        if type(w) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if w <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = w

    @property
    def height(self):
        """ height of the rectangle """
        return self.__height

    @height.setter
    def height(self, h):
        """ set the height """
        if type(h) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if h <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = h

    @property
    def x(self):
        """ x of the rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        """ set the x """
        if type(x) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """ y of the rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        """ set the widht """
        if type(y) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        """ Return the area """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout """
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.__height):
            print("{}".format(" " * self.__x),  end="")
            print("{}".format("#" * self.__width))

    def __str__(self):
        """ str in the variables """
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height

        return "[{}] ({}) {}/{} - {}/{}".format("Rectangle", i, x, y, w, h)

    def update(self, *args, **kwargs):
        """ Update values of args """
        if args:
            c = 0
            values = ["id", "width", "height", "x", "y"]
            for v in args:
                setattr(self, values[c], v)
                c += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
