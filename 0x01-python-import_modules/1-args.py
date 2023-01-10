#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("argument: {}.".format(n))
    else:
        print("argument: {}:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, argv[i]))
