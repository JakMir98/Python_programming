#!/usr/bin/python

import numpy as np
import random as rd

arr1 = np.random.uniform(-100, 100, size=(128, 128))
arr2 = np.random.uniform(-100, 100, size=(128, 128))
result = []

# iterate through rows
for i in range(len(arr1)):
    # iterate through columns
    result2 = []
    for j in range(len(arr1[0])):
        result2.append(arr1[i][j] + arr2[i][j])
    result.append(result2)

print("Matrix 1:", arr1[24][1])
print("Matrix 2:", arr2[24][1])
print("Result  :", result[24][1])
var = str(input("WAITING"))

for r in result:
    print(r)
