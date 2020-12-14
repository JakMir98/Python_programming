#!/usr/bin/python
key = str(input("Enter password\n"))

var = str(input("Enter password again\n"))

if var == key:
    print("You guessed it!")
else:
    print("Wrong")