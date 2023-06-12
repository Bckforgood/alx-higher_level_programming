#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        n_str += my_string[i]
    return n_str
