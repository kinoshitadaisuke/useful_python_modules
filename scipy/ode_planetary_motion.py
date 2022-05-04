#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/05/02 22:44:22 (CST) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.animation

# initialising a parser
desc   = 'solving equation of motion'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-x0', '--x0', type=float, default=1.0,
                     help='initial position in X (default: 1 au)')
parser.add_argument ('-y0', '--y0', type=float, default=0.0,
                     help='initial position in Y (default: 0 au)')
parser.add_argument ('-vx0', '--vx0', type=float, default=0.0,
                     help='initial velocity in X (default: 0 sqrt(GM)')
parser.add_argument ('-vy0', '--vy0', type=float, default=1.0,
                     help='initial velocity in Y (default: 1 sqrt(GM))')
parser.add_argument ('-M', '--M', type=float, default=1.0,
                     help='mass of star (default: 1 solar mass)')
parser.add_argument ('-t', '--time', type=float, default=10.0,
                     help='time of simulation (default: 10 yr)')
parser.add_argument ('-i', '--interval', type=float, default=0.01,
                     help='time interval of image creation (default: 0.01 yr)')
parser.add_argument ('-r', '--resolution', type=int, default=225, \
                     help='resolution of output file (default: 225 dpi)')
parser.add_argument ('-o', '--output', default='', \
                     help='output PNG file prefix')

# parsing arguments
args = parser.parse_args ()

# parameters
qx0           = args.x0
qy0           = args.y0
vx0           = args.vx0
vy0           = args.vy0
Mstar         = args.M
time_end      = args.time
dt            = args.interval
resolution    = args.resolution
output_prefix = args.output

# check of output_prefix
if (output_prefix == ''):
    print ("ERROR: output file prefix must be given!")
    sys.exit ()

#
# constants
#

# unit of time: year
# unit of distance: au

# gravitational constant
GM = 4.0 * numpy.pi * numpy.pi

#
# equation of motion
#
def eqmo (t, y):
    dy = numpy.zeros_like (y)
    r_cubed = ( y[0]**2 + y[2]**2 )**1.5
    dy[0] = y[1]
    dy[1] = -GM * y[0] / r_cubed
    dy[2] = y[3]
    dy[3] = -GM * y[2] / r_cubed
    return dy

# time to write position and velocity
n_step = int (time_end / dt) + 1
t_eval = numpy.linspace (0.0, time_end, n_step)

# initial values
y_init = (qx0, vx0  * numpy.sqrt (GM), qy0, vy0 * numpy.sqrt (GM))

# orbital integration
sol = scipy.integrate.solve_ivp (eqmo, [0.0, time_end], y_init, \
                                 t_eval=t_eval, dense_output=True, \
                                 rtol=10**-6, atol=10**-9)

# results (positions and velocities)
qx = sol.y[0]
qy = sol.y[2]
vx = sol.y[1]
vy = sol.y[3]

# finding maximum and minimum values
qx_min = +10**10
qx_max = -10**10
qy_min = +10**10
qy_max = -10**10
for i in range ( len (qx) ):
    if (qx[i] < qx_min):
        qx_min = qx[i]
    if (qx[i] > qx_max):
        qx_max = qx[i]
    if (qy[i] < qy_min):
        qy_min = qy[i]
    if (qy[i] > qy_max):
        qy_max = qy[i]
list_maxmin = [abs (qx_min), abs (qx_max), abs (qy_min), abs (qy_max)]
sorted_maxmin = sorted (list_maxmin)
x_min = -1.0 * sorted_maxmin[-1] * 1.2
x_max = +1.0 * sorted_maxmin[-1] * 1.2
y_min = -1.0 * sorted_maxmin[-1] * 1.2
y_max = +1.0 * sorted_maxmin[-1] * 1.2

# making plots
for i in range ( len (qx) ):
    print ("%08d %8.4f %8.4f %8.4f %8.4f" % (i, qx[i], qy[i], vx[i], vy[i]) )

    # output file name
    file_output = "%s_%08d.png" % (output_prefix, i)
    
    #
    # plotting using Matplotlib
    #
    
    # making objects "fig" and "ax"
    fig = matplotlib.figure.Figure ()
    matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax = fig.add_subplot (111)

    # axes
    ax.set_title ('Planetary Motion')
    ax.set_xlabel ('X [au]')
    ax.set_ylabel ('Y [au]')
    ax.set_xlim (x_min, x_max)
    ax.set_ylim (y_min, y_max)
    ax.set_aspect ('equal')

    # plotting a figure
    ax.plot (0.0, 0.0, color='yellow', marker='o', markersize=10, \
             label='star')
    if (i < 100):
        for j in range (i):
            ax.plot (qx[j], qy[j], color='cyan', marker='o', markersize=3, \
                     alpha=j/i)
    else:
        for j in range (100):
            ax.plot (qx[i-j], qy[i-j], color='cyan', marker='o', markersize=3, \
                     alpha=1.0-j/100.0)
    ax.plot (qx[0:i], qy[0:i], color='black', marker=',', alpha=0.5)
    ax.plot (qx[i], qy[i], color='green', marker='o', markersize=5, \
             label='planet')
    text_time = "Time: %8.2f year" % (i * dt)
    text_initial = "Initial conditions"
    text_mass    = "mass of star = %5.2f solar mass" % (Mstar)
    text_iq      = "(qx0, qy0) = (%4.2f au, %4.2f au)" \
        % (qx0, qy0)
    text_iv      = "(vx0, vy0) = (%4.2f au/yr, %4.2f au/yr)" \
        % (vx0 * numpy.sqrt (GM), vy0 * numpy.sqrt (GM))
    ax.text (0.03, 0.95, text_time, transform=ax.transAxes)
    ax.text (0.03, 0.18, text_initial, transform=ax.transAxes)
    ax.text (0.05, 0.13, text_mass, transform=ax.transAxes)
    ax.text (0.05, 0.08, text_iq, transform=ax.transAxes)
    ax.text (0.05, 0.03, text_iv, transform=ax.transAxes)
    ax.legend ()

    # saving the figure to a file
    fig.savefig (file_output, dpi=resolution)
