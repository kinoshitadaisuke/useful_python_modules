#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:20 (CST) daisuke>

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = (x+1) * (x-1)

# expanding f(x)
f2 = sympy.expand (f)

# printing result
print (f, "=", f2)
