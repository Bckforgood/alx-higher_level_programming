#!/usr/bin/python3
def uppercase(str):
    output = ""
    for c in str:
        ascii_value = ord(c)
        if ascii_value >= 97 and ascii_value <= 122:
            uppercase_value = ascii_value - 32
            output += "{}".format(chr(uppercase_value))
        else:
            output += "{}".format(c)
    print(output)
