#!/usr/bin/python3
"""
In a text file, there is a single
character H. Your text editor can
execute only two operations in
this file:
"""


def mul(n):
    """
    n :int
    """
    s = []
    r = 0
    if n == 2 or n == 3:
        return n
    for i in range(2, n // 2):
        if n % i == 0:
            r = i
    if r == 0:
        return n
    s.append(r)
    return s.append(mul(n // r))


def minOperations(n):
    """
    n : int
    _return_ :
    """
    if n <= 1:
        return 0
    s = mul(n)
    if type(s) == int:
        return s
    r = []
    for i in s:
        if type(i) != int:
            r.append(sum(i))
        else:
            r.append(i)
    return sum(r)
