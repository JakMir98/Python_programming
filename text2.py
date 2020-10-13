#!/usr/bin/python
import os
import re

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path_read = "Texts/artykul.txt"
rel_path_write = "Texts/artykul3.txt"
abs_file_path_read = os.path.join(script_dir, rel_path_read)
abs_file_path_write = os.path.join(script_dir, rel_path_write)

with open(abs_file_path_read, 'r') as f:
    data = f.read()

    dictionary = {"i": "oraz", "oraz": "i",
                  "nigdy": "prawie nigdy", "dlaczego": "czemu"}
    temp = data.split()
    res = []
    for wrd in temp:
        res.append(dictionary.get(wrd, wrd))

    res = ' '.join(res)

    _file = open(abs_file_path_write, "w")
    _file.write(res)
    _file.close()
