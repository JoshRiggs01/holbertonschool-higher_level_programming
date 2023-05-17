#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list: # check if list is empty
        return None
    max_int = my_list[0]
    for element in my_list:
        if element > max_int:
            max_int = element
    return max_int
