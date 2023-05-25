#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard
"""
import sys


def diagRigthBottom(point, n):
    line = []
    i, j = point
    if i < (n - 1) and j < (n - 1):
        while (i < (n - 1) or j < (n - 1)):
            line.extend([i, j])
            i += 1
            j += 1
    return line


def diagRigthTop(point, n):
    line = []
    i, j = point
    if i > 0 and j < n:
        while (i >= 0 and j < n):
            line.extend([i, j])
            i -= 1
            j += 1
    return line


def diagLeftBottom(point, n):
    line = []
    i, j = point
    if i < n and j > 0:
        while (i < n or j >= 0):
            line.extend([i, j])
            i += 1
            j -= 1
    return line


def diagLeftTop(point, n):
    line = []
    i, j = point
    if i >= 0 and j >= 0:
        while (i >= 0 or j >= 0):
            line.extend([i, j])
            i -= 1
            j -= 1
    return line


def nqueens():
    """n queens resolve"""
    if len(sys.argv) < 2:
        print('Usage: nqueens N, followed by a new line')
        exit(1)
    n = sys.argv[1]
    try:
        n = int(n)
    except Exception:
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    
    echiquier = [[i, j] for i in range(n) for j in range(n)]
    bad = []
    s = 0
    while(s < n):
        line = []
        for k in echiquier[s:n]:
            i, j = k
            if k not in line and (i not in bad or j not in bad):
                line.append(k)
                bad.extend(diagLeftBottom(k, n))
                bad.extend(diagLeftTop(k, n))
                bad.extend(diagRigthBottom(k, n))
                bad.extend(diagRigthTop(k, n))
        s += 1
        if len(line) == n:
            print(line)


if __name__ == '__main__':
    nqueens()