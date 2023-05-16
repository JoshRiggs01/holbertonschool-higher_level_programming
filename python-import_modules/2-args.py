#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    if n == 0:
        print("{} argument{}.".format(n, "" if n == 1 else "s"))
    else:
        n_args = n + 1 - (1 if n>0 else 0)
        print("{} argument{}:".format(n_args, "" if n_args == 1 else "s"))
        for i in range(1, n+1):
            print("{}: {}".format(i, sys.argv[i]))
