#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for a in set_1:
        if a not in set_2:
            diff.add(a)
    for i in set_2:
        if i not in set_1:
            diff.add(i)
    return diff
