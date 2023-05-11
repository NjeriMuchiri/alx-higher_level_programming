#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ments = len(sys.argv) - 1
    if ments != 3:
       print("Usage: ./100-my_calculator.py <a> <operator> <b>")
       sys.exit(1)
    oper = sys.argv[2]
    if oper != '+' and oper != '-' and '*' and oper != '/':
        print("Uknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    if oper == '+':
        print("{:d} + {:d}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{:d} - {:d}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{:d} * {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d}".format(a, b, div(a, b)))
