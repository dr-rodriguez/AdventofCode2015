"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf
at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one
house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a
little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
"""

print 'Part 1'

# Read in input
f = open('files/input_d3.txt', 'r')

# Trying brute-force approach: create a big grid of zeros
import numpy as np
arrsize = 1000
grid = np.zeros([arrsize,arrsize])
xloc = arrsize/2
yloc = arrsize/2

travelcommands = f.readline()

grid[xloc,yloc] = 1
for move in travelcommands:
    if(move=='^'): yloc+=1
    if(move=='v'): yloc-=1
    if(move=='>'): xloc+=1
    if(move=='<'): xloc-=1
    grid[xloc,yloc] = 1

print grid.sum()
f.close()

"""The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?
"""

print 'Part 2'

# Re-read in input
f = open('files/input_d3.txt', 'r')

# Resetting the grid
grid = np.zeros([arrsize,arrsize])
xs = arrsize/2
ys = arrsize/2
xr = xs #robo-santa coords
yr = ys

travelcommands = f.readline()

grid[xs,ys] = 2 # both Santa and Robo-Santa start here
movecount = 0
for move in travelcommands:
    xstep = 0
    ystep = 0

    if(move=='^'): ystep = 1
    if(move=='v'): ystep = -1
    if(move=='>'): xstep = 1
    if(move=='<'): xstep = -1

    # Decide who moves
    if(movecount % 2==0):
        print 'Santa moves ', xstep, ystep, '(',move,') to: ', xs+xstep, ys+ystep
        xs += xstep
        ys += ystep
        grid[xs,ys] = 1
    else:
        print 'Robo-Santa moves ', xstep, ystep, '(',move,') to: ', xr+xstep, yr+ystep
        xr += xstep
        yr += ystep
        grid[xr,yr] = 1

    movecount += 1

print grid.sum()
f.close()