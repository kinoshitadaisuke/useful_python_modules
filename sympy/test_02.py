#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:25 (CST) daisuke>

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = sympy.sin (x) / x

# lim (x -> 0) sin(x)/x
lim_0 = sympy.limit (f, x, 0)

# printing result
print ("lim_0 sin(x)/x =", lim_0)
