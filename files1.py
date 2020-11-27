#!/usr/bin/python

import os

path, dirs, files = next(os.walk("/dev"))
file_count = len(files)
print("Number of files in directoryy \"/dev\":", file_count)
