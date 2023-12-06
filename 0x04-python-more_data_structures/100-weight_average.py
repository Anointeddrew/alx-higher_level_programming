#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    enum = 0
    lade = 0

    for tup in my_list:
        enum += tup[0] * tup[1]
        lade += tup[1]

    return (enum / lade)
