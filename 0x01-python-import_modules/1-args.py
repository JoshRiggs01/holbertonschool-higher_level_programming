#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("{} {}:".format(n + 1, argv[n]))
    else:
        print("{} arguments:".format(n + 1, argv[n]))
        for i in range(n):
            print("{}: {}".format(i + 1, argv[i]))
