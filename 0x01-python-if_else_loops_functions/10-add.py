#!/usr/bin/python3
def add(a, b):
    while b != 0:
        sum_without_carry = a ^ b
        carry = (a & b) << 1
        a = sum_without_carry
        b = carry
    return a
