#!/usr/bin/python3

import sys
if len(sys.argv)!=4:
    sys.exit("Error, no hay 4 elementos")
_, operacion, op1,op2 = sys.argv

op1 = float(op1)
op2 = float(op2)

if operacion == "suma":
    print(op1 + op2)
elif operacion == "resta":
    print(op1 -op2)
elif operacion == "division":
    try:
        print(op1/op2)
    except ZeroDivisionError:
        print("No me dividas entre cero")
elif operacion == "mult":
    print(op1 *op2)
else:
    print("Operacion incorrecta")
