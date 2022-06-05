#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_my_list = len(my_list)
    new_copy = my_list.copy()
    if idx < 0 or idx > len_my_list - 1:
        return new_copy
    else:
        new_copy[idx] = element
        return new_copy

