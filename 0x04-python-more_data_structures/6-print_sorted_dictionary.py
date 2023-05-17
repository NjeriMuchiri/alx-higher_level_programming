#!/usr/bin/python3
def print_sorted_dictionary(a_dictionay):
    orde_red = list(a_dictionay.keys())
    orde_red.sort()
    for i in orde_red:
        print("{}: {}".format(i, a_dictionay.get(i)))
