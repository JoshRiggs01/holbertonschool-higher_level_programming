#!/usr/bin/python3
"""
prints a string, if string ends with . ? :
then it will be followed by 2 new lines
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
