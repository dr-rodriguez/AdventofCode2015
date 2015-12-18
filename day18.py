"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now,
at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration.
With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input).
A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""

import numpy as np

# Read in and parse the file
f = open('files/input_d18.txt','r')
grid = []
#A # means "on", and a . means "off".
for line in f:
    row = []
    for elem in line.strip():
        if elem=='#':
            x = 1
        else:
            x = 0

        row.append(x)
    grid.append(row)
f.close()

grid = np.array(grid)

# ===========================================================================

# Function to process an element
def process_element(val, grid, i0, j0):

    imin = i0-1 if (i0>0) else 0
    imax = i0+1 if (i0<99) else 99
    jmin = j0-1 if (j0>0) else 0
    jmax = j0+1 if (j0<99) else 99

    #print imin, imax, jmin, jmax
    count = 0
    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if i==i0 and j==j0:
                continue
            else:
                #print i, j, grid[i,j]
                count += grid[i,j]

    #print count
    # Turn lights on or off
    newval = val
    if val==1: #if already on
        if count==2 or count==3:
            newval = 1
        else:
            newval =0
    else:
        if count==3:
            newval = 1
        else:
            newval = 0

    return newval

# ===========================================================================

# Function to process grid
def process_grid(grid):
    newgrid = grid*0

    for i in range(100):
        for j in range(100):
            newgrid[i,j] = process_element(grid[i,j], grid, i, j)

    return newgrid

#print grid[10,13]
#print process_element(grid[10,13], grid, 10, 13)

# ===========================================================================

grid2 = grid
for i in range(100):
    grid = process_grid(grid)
print 'Part 1 Answer:', i, grid.sum()

"""
--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is all just an
implementation of Conway's Game of Life. At least, it was, until you notice that something's
wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and
can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four
corners always in the on state, how many lights are on after 100 steps?
"""

# Function to process grid
def process_grid2(grid):
    newgrid = grid*0

    for i in range(100):
        for j in range(100):
            if (i==0 and j==0) or (i==0 and j==99) or (i==99 and j==0) or (i==99 and j==99):
                newgrid[i,j] = 1
            else:
                newgrid[i,j] = process_element(grid[i,j], grid, i, j)

    return newgrid

for i in range(100):
    grid2 = process_grid2(grid2)
print 'Part 2 Answer:', i, grid2.sum()