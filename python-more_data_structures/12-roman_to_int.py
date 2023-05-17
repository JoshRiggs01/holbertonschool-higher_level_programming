#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    prev_value = 0
    for char in roman_string[::-1]:
        current_value = roman_values[char]
        if prev_value > current_value:
            int_value -= current_value
        else:
            int_value += current_value
        prev_value = current_value
    return int_value
