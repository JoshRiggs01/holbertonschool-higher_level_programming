#!/usr/bin/python3
output = ''
for i in range(100):
    output += "{:02}, ".format(i) if i != 99 else "{:02}\n".format(i)
print(output, end='')
