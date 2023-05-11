#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{:d} + {:d} =  ".format(a, b), end='')
print(add(a, b))
print("{:d} + {:d} =  ".format(a, b), end='')
print(sub(a, b))
print("{:d} + {:d} =  ".format(a, b), end='')
print(mul(a, b))
print("{:d} + {:d} =  ".format(a, b), end='')
print(div(a, b))
