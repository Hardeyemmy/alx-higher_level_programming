#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        len_my_list = len(my_list)
        my_list.reverse()
        for list in range(len_my_list):
            print("{:d}".format(my_list[list]))
