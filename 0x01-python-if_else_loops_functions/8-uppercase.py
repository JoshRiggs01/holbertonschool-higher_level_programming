#!/usr/bin/python3
def uppercase(s):
    output = ''.join([chr(ord(i) - 32) if ord(i) in range(97, 123) else i for i in s])
    print("{}".format(output))
