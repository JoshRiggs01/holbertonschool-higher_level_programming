#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("The number {} is positive\n".format(number))
elif number == 0:
    print("The number {} is zero\n".format(number))
else:
    print("The number {} is negative\n".format(number))
