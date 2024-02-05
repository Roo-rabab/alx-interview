#!/usr/bin/python3
"""A module for working with Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # return trianlgle if n <= 0
    if n <= 0:
        return triangle
    for i in range(n):
        list_ = []

        for j in range(i+1):
            if j == 0 or j == i:
                list_.append(1)
            else:
                list_.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(list_)
    # print triangle
    return triangle
