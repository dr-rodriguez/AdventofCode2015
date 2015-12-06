"""
You just finish implementing your winning light pattern when you realize you mistranslated
Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can
have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?
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

    # Load through the grid elements and increase/decrease brightness
    for i in range(xs,xe+1):
        for j in range(ys,ye+1):
            val = grid[i,j]

            if go_on:
                grid[i,j] = val + 1
            else:
                grid[i,j] = val - 1
                if grid[i,j] <0: grid[i,j] = 0 # Don't go below zero

            if toggle:
                grid[i,j] = val + 2



f.close()
print 'Part 2 Answer: ', grid.sum()