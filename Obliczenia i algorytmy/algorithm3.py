#!/usr/bin/python

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

if(len(a) == len(b)):
    c = 0
    for i in range(len(a)):
        c = c + a[i]*b[i]
        print(c)
    print("C =", c)

c = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3]
print(c)
