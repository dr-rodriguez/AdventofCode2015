"""
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the
distances between every pair of locations. He can start and end at any two (different)
locations he wants, but he must visit each location exactly once. What is the shortest
distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

import random


# ========================================================
# Loop through the location list and match them
def processtravel(curr_loc, newtext, loc_copy, newdist):
    # Loop through random lines in file
    for line in newtext:
        elems = line.split()
        loc1 = elems[0]
        loc2 = elems[2]
        distval = float(elems[-1])
        #print curr_loc, loc1, loc2

        # Add distance and pop location when visited
        if (loc1==curr_loc) and loc2 in loc_copy:
            newdist += distval
            curr_loc = loc2
            #print 'Removing (loc1): ', loc1, ' New Loc: ', curr_loc, ' Dist: ', newdist
            loc_copy.remove(loc1)
        elif (loc2==curr_loc) and loc1 in loc_copy:
            newdist += distval
            curr_loc = loc1
            #print 'Removing (loc2): ', loc2, ' New Loc: ', curr_loc, ' Dist: ', newdist
            #print loc_copy
            loc_copy.remove(loc2)

    return newdist, curr_loc, loc_copy

# ========================================================
# Function to process Santa's travel
def santatravel(newtext, all_loc):
    loc_copy = all_loc
    random.shuffle(loc_copy)
    random.shuffle(newtext)

    curr_loc = loc_copy[0]
    #print curr_loc

    # Continue until all locations are visited
    count = 0
    newdist = 0
    while len(loc_copy)>1:
        #print loc_copy
        newdist, curr_loc, loc_copy = processtravel(curr_loc, newtext, loc_copy, newdist)
        count += 1
        # If count exceeds 1000, assume we failed to converge
        if count>1000:
            newdist = 9999
            break

    #print loc_copy

    return newdist

# ========================================================
# Recreate the list of locations
def regenloclist(alltext):
    global all_loc
    for line in alltext:
        elems = line.split()
        curr_loc = elems[0]
        if curr_loc not in all_loc: all_loc.append(curr_loc)
        curr_loc = elems[2]
        if curr_loc not in all_loc: all_loc.append(curr_loc)

    return all_loc


# ========================================================
# Read the input file
f = open('files/input_d9.txt','r')
alltext = f.read().split('\n')[:-1]
#print alltext
f.close()

# Get list of all locations
all_loc = []
all_loc = regenloclist(alltext)

print all_loc

# Set random seed
random.seed()

bestdist = 251+1
dist = 9999
count = 0
while dist>bestdist:
    dist = santatravel(alltext, all_loc)
    all_loc = regenloclist(alltext)
    #print dist
    if dist<bestdist:
        bestdist = dist
        dist += 1

    count += 1
    if count>10000: break

# Compare max distances
print 'Part 1 Answer: ', bestdist

# Part 2
"""
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""

bestdist = 898-1
dist = 0
count = 0
while dist < bestdist:
    dist = santatravel(alltext, all_loc)
    all_loc = regenloclist(alltext)
    #print dist
    if dist > bestdist:
        bestdist = dist
        dist -= 1

    count += 1
    if count > 10000: break

# Compare max distances
print 'Part 2 Answer: ', bestdist

