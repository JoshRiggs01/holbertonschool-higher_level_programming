#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    if n == 0:
        print("{} argument:".format(n+1))
        print("1: {}".format(sys.argv[0]))
    else:
        print("{} arguments:".format(n+1 - (1 if n>0 else 0)))
        for i in range(1, n+1):
            print("{}: {}".format(i, sys.argv[i]))
