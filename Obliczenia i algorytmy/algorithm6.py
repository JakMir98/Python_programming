#!/usr/bin/python

import numpy as np
import random as rd


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c] * \
            getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def minor(array, i, j):
    c = array
    c = c[:i] + c[i+1:]
    for k in range(0, len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c


def det(array, n):
    if n == 1:
        return array[0][0]
    if n == 2:
        return array[0][0]*array[1][1] - array[0][1]*array[1][0]
    sum = 0
    for i in range(0, n):
        m = minor(array, 0, i)
        sum = sum + ((-1)**i)*array[0][i] * det(m, n-1)
    return sum


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total


dimen = int(input("Enter dimension of matrix "))
arr1 = np.random.uniform(-100, 100, size=(dimen, dimen))
print(arr1)
print(np.linalg.det(arr1))
print(determinant_recursive(arr1))
# print(getMatrixDeternminant(arr1))
#print(det(arr1, len(arr1)))
