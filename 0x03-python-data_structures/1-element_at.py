#!/usr/bin/python3
def element_at(my_list, idx):
    len_my_list = len(my_list)
    if idx < 0 or idx > len_my_list - 1:
        print('None')
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
