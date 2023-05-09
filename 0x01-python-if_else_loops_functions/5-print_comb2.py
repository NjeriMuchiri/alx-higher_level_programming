#!/usr/bin/python3
for numbe in range(0, 100):
    if numbe != 99:
        print("{:02d}, ".format(numbe), end='')
    else:
        print("{:02d}".format(numbe))
