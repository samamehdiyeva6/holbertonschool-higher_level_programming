#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in new_matrix:
        for j in range(0, len(i)):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    return new_matrix
