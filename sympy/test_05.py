#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:38 (CST) daisuke>

# importing sympy module
import sympy

# variable
x, y = sympy.symbols ('x y')

# function f(x,y)
f = (x+y)**2 - (x-y)**2

# solving f(x) = 0
f2 = sympy.simplify (f)

# printing result
print (f, "=", f2)
