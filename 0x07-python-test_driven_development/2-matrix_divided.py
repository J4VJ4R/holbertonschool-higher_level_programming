#!/usr/bin/python3
""" 
This is a function it does
a different tests with the use 
edge cases.
"""


def matrix_divide(matrix, div):
    """ this is a function that
    divides all elements of a matrix
    """

    e = "matrix must be a matrix (list of lists) of integers/floats"
    
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError(e)

    for i in matrix
        if len(i) == 0:
            raise TypeError(e)
        for j in matrix:
            if type(j) != int and type(j) != float:
                raise TypeError(e)
    listReload = []
    for s in matrix:
        listReload.append(len(s))
    if not all(item == listReload[0] for item in listReload):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in j] for j in matrix]

    return new_matrix
