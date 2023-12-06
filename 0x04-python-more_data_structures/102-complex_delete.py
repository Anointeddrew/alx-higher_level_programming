#!/usr/bin/python3
def complex_delete(my_dict, value):
    gsd = my_dict.copy()
    for k, l in gsd.items():
        if value == l:
            my_dict.pop(k)
    return my_dict
