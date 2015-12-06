"""
Because your neighbors keep defeating you in the holiday house decorating contest year after year,
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how
to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at
0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle,
inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.
"""

import numpy as np

# Read input file
f = open('files/input_d6.txt','r')

grid = np.zeros([1000,1000])

for line in f:
    elems = line.split()
    #print elems

    # Check: turn on or off
    go_on = False
    if elems[0]=='turn':
        indstart = 2
        if elems[1]=='on':
            go_on = True
        else:
            go_on = False

    # Check: toggle
    toggle = False
    if elems[0]=='toggle':
        indstart = 1
        toggle = True

    # Grab first coordinate
    xs,ys = elems[indstart].split(',')
    # Grab final coordinate
    xe,ye = elems[-1].split(',')

    # Convert to int
    xs = int(xs)
    xe = int(xe)
    ys = int(ys)
    ye = int(ye)

    # Load through the grid elements and turn on/off or toggle lights
    for i in range(xs,xe+1):
        for j in range(ys,ye+1):
            val = grid[i,j]

            if go_on:
                grid[i,j] = 1
            else:
                grid[i,j] = 0

            if toggle:
                if val==1:
                    grid[i,j] = 0
                else:
                    grid[i,j] = 1


f.close()
print 'Part 1 Answer: ', grid.sum()