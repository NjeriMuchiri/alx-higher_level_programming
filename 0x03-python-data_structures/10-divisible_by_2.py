#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_isbles = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_isbles.append(True)
        else:
            div_isbles.append(False)
    return (div_isbles)
