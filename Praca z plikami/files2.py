#!/usr/bin/python

import os


def get_current_path():
    return os.path.dirname(os.path.realpath(__file__))


def print_list(directory, depth):

    elements_list = os.listdir(directory)

    for element in elements_list:
        full_path = os.path.join(directory, element)
        line = ""
        for i in range(depth):
            line += "  "
        if os.path.isdir(full_path):
            print(line + element)
            print_list(full_path, depth + 1)
        else:
            print(line + element)


print_list(get_current_path(), 0)
