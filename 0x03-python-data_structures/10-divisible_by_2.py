#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multi.app(True)
        else:
            multi.app(False)

    return (multi)
