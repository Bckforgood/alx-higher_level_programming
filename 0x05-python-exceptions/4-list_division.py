#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for n in range(0, list_length):
        try:
            division_result = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("Wrong type")
            division_result = 0
        except ZeroDivisionError:
            print("Division by zero")
            division_result = 0
        except IndexError:
            print("Index out of range")
            division_result = 0
        finally:
            result_list.append(division_result)
    return result_list

