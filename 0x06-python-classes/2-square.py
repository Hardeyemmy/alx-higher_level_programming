#!/usr/bin/python3
class Square:
    """ Defines a square """
    def __init__(self, size):
        if type(size) != int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size