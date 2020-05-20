#!/usr/bin/python3
"""This class define a square."""


class Square:
    """Here you can write attributes
    and methods."""
    def __init__(self, size=0):
        """Create a square.

        Args:
            size (int): Size of the square.
        """
        self.size = size
    @property
    def size(self):
        """Get/set the actual size for the square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)
