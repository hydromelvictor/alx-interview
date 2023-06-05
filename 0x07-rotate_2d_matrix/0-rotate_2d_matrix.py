#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    matrix: Dict[Dict]
    """
    matrix_ = matrix[:]
    matrix.clear()
    i = 0
    for i in range(len(matrix_)):
        cols = []
        for line in matrix_:
            cols.append(line[i])
        matrix.append(cols[-1::-1])
        i += 1
