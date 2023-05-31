#!/usr/bin/python3
"""
    script that adds all arguments to a Python list,
    and then save them to a file:
    You must use your function save_to_json_file from
    7-save_to_json_file.py
    You must use your function load_from_json_file
    from 8-load_from_json_file.py
    The list must be saved as a JSON representation
    in a file named add_item.json
    If the file t exist, it should be created
    You t need to manage file permissions / exceptions.
"""


import sys
import os.path
from typing import List

def load_from_json_file(filename: str) -> List:
    import json
    if os.path.isfile(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_to_json_file(my_obj: List, filename: str):
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

if __name__ == '__main__':
    save_to_json_file(load_from_json_file("add_item.json") + sys.argv[1:], "add_item.json")
