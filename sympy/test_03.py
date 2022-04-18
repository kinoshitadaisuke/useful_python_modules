#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:01:29 (CST) daisuke>

# importing sympy module
import sympy

# variable
x, a, b, c = sympy.symbols ('x a b c')

# function f(x)
f = a*x**2 + b*x + c

# solving f(x) = 0
sol = sympy.solve (f, x)

# printing result
print ("x =", sol)
