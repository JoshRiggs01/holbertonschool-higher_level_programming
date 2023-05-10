#!/usr/bin/python3
output = ''
for i in range(10):
    for j in range(10):
        if i != j:
            output += "{}{}, ".format(i, j) if i < j else "{}{}, ".format(j, i)
print(output[:-2]+'\n', end='')
