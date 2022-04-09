#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/09 09:01:07 (CST) daisuke>

#
# a sample script to use uncertainties module
#

import uncertainties

a = uncertainties.ufloat (10.0, 3.0)
b = uncertainties.ufloat (15.0, 4.0)

c = a + b

print ("a =", a)
print ("b =", b)
print ("c = a + b =", c)

print ("sqrt (3.0**2 + 4.0**2) =", (3.0**2 + 4.0**2)**0.5)

print ()

d = uncertainties.ufloat (2.0, 0.6)
e = uncertainties.ufloat (3.0, 1.2)

f = d * e

print ("d =", d)
print ("e =", e)
print ("f = d * e =", f)

print ("sqrt ( (0.6/2.0)**2 + (1.2/3.0)**2 ) * (2.0 * 3.0) =", \
       ( (0.6/2.0)**2 + (1.2/3.0)**2 )**0.5 * (2.0 * 3.0) )
