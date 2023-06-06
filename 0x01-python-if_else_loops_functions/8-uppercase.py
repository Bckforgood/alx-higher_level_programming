#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_value = ord(c)
        if ascii_value >= 97 and ascii_value <= 122:
            uppercase_value = ascii_value - 32
            print("{}".format(chr(uppercase_value)), end="")
        else:
            print("{}".format(c), end="")
    print()
