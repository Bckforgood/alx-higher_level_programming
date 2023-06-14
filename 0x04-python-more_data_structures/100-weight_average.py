#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    total_value = 0
    total_weight = 0
    for item in my_list:
        total_value += item[0] * item[1]
        total_weight += item[1]
    return total_value / total_weight
