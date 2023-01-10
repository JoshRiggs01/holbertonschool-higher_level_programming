#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    return int(str(last_digit) + str(last_digit))
