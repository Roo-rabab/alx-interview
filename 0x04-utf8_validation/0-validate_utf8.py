#!/usr/bin/python3
"""UTF-8 validation module:
A method that determines if a given data set represents a valid UTF-8 encoding
-Prototype: def validUTF8(data)
-Return: True if data is a valid UTF-8 encoding, else return False
-A character in UTF-8 can be 1 to 4 bytes long
-The data set can contain multiple characters
-The data will be represented by a list of integers
-Each integer represents 1 byte of data, therefore you only need to handle
 the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Checks if a given data (list of integers) set represents a
    valid UTF-8 encoding.

    Args:
        data (list[int]): a list of integers
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
