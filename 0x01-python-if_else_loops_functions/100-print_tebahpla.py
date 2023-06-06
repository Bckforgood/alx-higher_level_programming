#!/usr/bin/python3
output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    output += "{}{}".format(chr(i), chr(i - 32) if i % 2 == 1 else "")
print(output, end='')
