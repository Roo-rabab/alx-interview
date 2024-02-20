#!/usr/bin/python3
"""The minimum operations coding challenge.
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    count_nOps = 0
    minOps = 2
    while n > 1:
        while n % minOps == 0:
            count_nOps += minOps
            n /= minOps
        minOps += 1
    return count_nOps
