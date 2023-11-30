#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num = len(args)

    if num == 0:
        print("0 arguments.")
    else:
        p = "s" if num > 1 else ""
        print("{:d} argument{:s}:".format(num, p))

        for i, arg in enumerate(args, start=1):
            print("{:d}: {}".format(i, arg))
