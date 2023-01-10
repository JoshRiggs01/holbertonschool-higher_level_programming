#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("Number of argument(s): {}.".format(n))
    else:
        print("Number of argument(s): {}:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, argv[i]))
