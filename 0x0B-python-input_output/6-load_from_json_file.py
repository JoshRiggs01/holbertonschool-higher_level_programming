#!/usr/bin/python3
"""
    function that creates an Object from JSON :
    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You t need to manage exceptions if the JSON string
    t represent an object.
    You t need to manage file permissions / exceptions.
"""


import json


def load_from_json_file(filename):
    """ creates a pythonobject from json file """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
