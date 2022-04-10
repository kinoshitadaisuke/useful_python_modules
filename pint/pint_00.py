#!/usr/pkg/bin/python3.9

# Time-stamp: <2022/04/10 10:39:00 (CST) daisuke>

import pint

#
# units
#

ur       = pint.UnitRegistry ()
u_deg    = ur.degree
u_rad    = ur.radian
u_arcmin = ur.arcmin
u_arcsec = ur.arcsec
u_mas    = ur.mas
u_pc     = ur.pc
u_au     = ur.au
u_m      = ur.metre

# angle a

angle_a = 180.0 * u_deg
angle_a_rad = angle_a.to (u_rad)
print ("angle_a = %s = %s" % (angle_a, angle_a_rad) )

# angle b

angle_b        = 1.0 * u_deg
angle_b_deg    = angle_b.to (u_deg)
angle_b_arcmin = angle_b.to (u_arcmin)
angle_b_arcsec = angle_b.to (u_arcsec)
print ("angle_b = %s = %s = %s" % (angle_b, angle_b_arcmin, angle_b_arcsec) )

# distance to Sirius
parallax = 374.5 * u_mas
distance = 1.0 / parallax.to (u_arcsec) * u_pc * u_arcsec
print ("distance to Sirius = %s" % distance)
print ("                   = %s" % distance.to (u_au) )
print ("                   = %s" % distance.to (u_m) )
