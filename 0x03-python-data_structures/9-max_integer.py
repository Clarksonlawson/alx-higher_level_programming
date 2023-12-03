#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n

    return max_num
