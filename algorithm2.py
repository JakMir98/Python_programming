#!/usr/bin/python
import numpy as np

np.random.seed()
alist = np.random.randint(0, 1000, size=50)
blist = sorted(alist, reverse=True)

for i in range(0, len(alist)):  # Bubble sort
    for j in range(i+1, len(alist)):
        if alist[i] < alist[j]:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp

print("My sorting:", alist)
print("Default sorting:", blist)
