#!/usr/bin/python3
"""area of a square"""


class Square:
    """square size"""
    def _init_(self, size=0):
        """constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self .__size = size
    def area(self):
        """area of square"""
        return (self._size * self._size)
