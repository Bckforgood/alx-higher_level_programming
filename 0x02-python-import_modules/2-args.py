#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ct = len(sys.argv) - 1
    if ct == 0:
        print("0 arguments.")
    elif ct == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ct))
    for i in range(ct):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
