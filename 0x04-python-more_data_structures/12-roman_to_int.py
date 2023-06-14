#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    next_roman = ''
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_nums:
            current_roman = roman_string[i]
            if i < len(roman_string) - 1:
                next_roman = roman_string[i + 1]
            if i == len(roman_string) - 1:
                result += roman_nums[current_roman]
            elif roman_nums[current_roman] < roman_nums[next_roman]:
                result -= roman_nums[current_roman]
            else:
                result += roman_nums[current_roman]
    return result
