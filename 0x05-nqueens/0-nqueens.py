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
    tr = 0
    # boucle parcours n fois
    while tr < n:
        line = []
        bad = []
        for pos in ech[tr:]:
            p, q = pos
            if pos not in line and p not in bad and q not in bas:
                line.append(pos)
                bad.extend(diagLeftTop(pos, n))
                bad.extend(diagLeftBottom(pos, n))
                bad.extend(diagRigthTop(pos, n))
                bad.extend(diagRigthBottom(pos, n))
        if len(line) == n:
            print(line)
        tr += 1


if __name__ == '__main__':
    nqueens()
