#!/usr/bin/python3
def uppercase(s):
    output = ''
    for i in s:
        if ord(i) in range(97, 123):
            output += chr(ord(i) - 32)
        else:
            output += i
    print(output, end='\n')
