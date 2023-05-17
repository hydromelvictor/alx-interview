#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    data : str
    return true or false
    """
    i = 0
    count = len(data)

    while i < count:
        byte = data[i]
        if byte & 0b10000000 == 0b00000000:
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            if i + 1 >= count or data[i + 1] & 0b11000000 != 0b10000000:
                return False
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            if i + 2 >= count or any((data[i + j + 1] & 0b11000000) != 0b10000000 for j in range(2)):
                return False
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            if i + 3 >= count or any((data[i + j + 1] & 0b11000000) != 0b10000000 for j in range(3)):
                return False
            i += 4
        else:
            return False
    return True

