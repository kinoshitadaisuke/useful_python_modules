#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:34 (CST) daisuke>

# importing sympy module
import sympy

# variable
x, y, k = sympy.symbols ('x y k')

# function y(x)
y = sympy.Function ('y')

# solving dy/dx = -ky
sol = sympy.dsolve (sympy.Eq (y(x).diff (x), -k*y(x)), y(x))

# printing result
print ("y =", sol)
