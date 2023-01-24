#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def _init_(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""
        super()._init_(size, size, x, y, id)

    def _str_(self):
        """return string representation of Rectangle"""
        return '[' + type(self)._name_ + '] (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - ' \
            + str(self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        key = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, key[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of
        Rectangle instance
        """
        selfDict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return selfDict

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for __size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
