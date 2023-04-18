#!/usr/bin/python3
"""
pascal triangle
"""


def fac(n):
    """
    factoriel de n
    """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def cmb(k, n):
    """
    combinaison
    """
    return fac(n) // (fac(n-k) * fac(k))


def pascal_triangle(n):
    """
    n: integer
     __return__
    """
    res = []
    if n > 0:
        for i in range(n):
            res.append([cmb(k, i) for k in range(i + 1)])
    return res
