#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:15 (CST) daisuke>

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = sympy.exp (-x**2)

# integration of f(x)
I = sympy.integrate (f, (x, -sympy.oo, sympy.oo))

# printing result
print (I)
