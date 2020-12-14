#!/usr/bin/python

import numpy as np
import random as rd

arr1 = np.random.uniform(-100, 100, size=(8, 8))
arr2 = np.random.uniform(-100, 100, size=(8, 8))
result = np.zeros((8, 8))
print("1 array:")
print(arr1)
print("\n2 array:")
print(arr2)
print("\nResult array:")
print(result)

# iterate through rows of X
for i in range(len(arr1)):
    # iterate through columns of Y
    for j in range(len(arr2[0])):
        # iterate through rows of Y
        for k in range(len(arr2)):
            result[i][j] += arr1[i][k] * arr2[k][j]

print("\nFinal result array:")
for r in result:
    print(r)
