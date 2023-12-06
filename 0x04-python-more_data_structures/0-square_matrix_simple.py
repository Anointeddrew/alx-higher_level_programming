#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    quadrate = []
    for line in matrix:
        quadrate.append([c**2 for c in line])
    return quadrate
