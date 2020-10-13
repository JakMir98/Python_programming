#!/usr/bin/python
import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path_read = "Texts/artykul.txt"  # load file
rel_path_write = "Texts/artykul2.txt"  # save file
abs_file_path_read = os.path.join(script_dir, rel_path_read)
abs_file_path_write = os.path.join(script_dir, rel_path_write)

with open(abs_file_path_read, 'r') as f:
    data = f.read()
    var = data.replace("się", "").replace("i", "").replace(
        "oraz", "").replace("nigdy", "").replace("dlaczego", "")

    _file = open(abs_file_path_write, "w")
    _file.write(var)
    _file.close()
