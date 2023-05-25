#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard
"""
import sys


def diagLeftBottom(pos, n):
    line = []
    p, q = pos
    while p < (n - 1) or q > 0:
        line.append(p)
        line.append(q)
        p += 1
        q -= 1
    return line


def diagLeftTop(pos, n):
    line = []
    p, q = pos
    while p > 0 or q > 0:
        line.append(p)
        line.append(q)
        p -= 1
        q -= 1
    return line


def diagRigthBottom(pos, n):
    line = []
    p, q = pos
    while p < (n - 1) or q < (n - 1):
        line.append(p)
        line.append(q)
        p += 1
        q += 1
    return line


def diagRigthTop(pos, n):
    line = []
    p, q = pos
    while p > 0 or q < (n - 1):
        line.append(p)
        line.append(q)
        p -= 1
        q += 1
    return line


def nqueens():
    """n queens algorithms"""
    str = sys.argv
    if len(str) < 2:
        print('Usage: nqueens N')
        exit(1)
    n = str[1]
    try:
        n = int(n)
    except Exception:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    # toutes les positions de l'echiquier
    ech = [[i, j] for i in range(n) for j in range(n)]
    prs = [k for k in ech[:n]]

    for elt in prs:
        res = ech[:]
        p, q = tuple(elt)
        for _row in res:
            if p in _row or q in _row:
                res.remove(_row)
            for z in diagLeftBottom(elt, n):
                if z in _row:
                    res.remove(_row)
            for z in diagLeftTop(elt, n):
                if z in _row:
                    res.remove(_row)
            for z in diagRigthBottom(elt, n):
                if z in _row:
                    res.remove(_row)
            for z in diagRigthTop(elt, n):
                if z in _row:
                    res.remove(_row)
        if len(res) == n:
            print(res)


if __name__ == '__main__':
    nqueens()
