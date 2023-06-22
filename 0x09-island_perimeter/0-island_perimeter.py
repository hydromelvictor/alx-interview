#!/usr/bin/python3
""" perimeter """


def island_perimeter(grid):
    """
    parameters
    ==========
    grid: List[list]
    __return__ : int
    """
    # cellule carre c = 1
    # liaison horizontal et vertical
    x = len(grid)
    y = len(grid[0])
    prim = 0
    for i in range(x):
        for j in range(y):
            k = grid[i][j]
            if k == 1:
                if (i != 0 and grid[i - 1][j] == 0) or i == 0:
                    prim += 1
                if (i != x - 1 and grid[i + 1][j] == 0) or i == x - 1:
                    prim += 1
                if (j != 0 and grid[i][j - 1] == 0) or j == 0:
                    prim += 1
                if (j != y - 1 and grid[i][j + 1] == 0) or j == y - 1:
                    prim += 1
    return prim
