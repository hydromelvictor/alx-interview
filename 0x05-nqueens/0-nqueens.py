#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard
"""
import sys


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
    
    if n % 2 != 0:
        print([[]])
        exit(1)

    for k in range(n):
        line = []
        for l in range(n):
            if k != l and k + l != n - 1:
                line.append([k, l])
        print(line)


if __name__ == '__main__':
    nqueens()