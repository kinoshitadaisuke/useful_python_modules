#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/18 21:08:41 (CST) daisuke>

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function y(x)
y = sympy.Function ('y')

# differential equation
lane_emden_0 = sympy.Eq (x**-2 * (x**2 * y(x).diff (x)).diff (x), -1)

# solving lane-emden equation of n=0
sol = sympy.dsolve (lane_emden_0, y(x))

# printing result
print ("y =", sol)
