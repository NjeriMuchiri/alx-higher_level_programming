#!/usr/bin/python3
for numbe in range(0, 99):
    if numbe % 10 > numbe / 10:
        if numbe != 89:
            print("{:02d}, ".format(numbe), end='')
        else:
            print("{:02d}".format(numbe))
