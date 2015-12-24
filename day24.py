"""
--- Day 24: It Hangs in the Balance ---

It's Christmas Eve, and Santa is loading up the sleigh for this year's deliveries.
However, there's one small problem: he can't get the sleigh to balance.
If it isn't balanced, he can't defy physics, and nobody gets presents this year.

No pressure.

Santa has provided you a list of the weights of every package he needs to fit on the sleigh.
The packages need to be split into three groups of exactly the same weight, and every package has to fit.
The first group goes in the passenger compartment of the sleigh,
and the second and third go in containers on either side.
Only when all three groups weigh exactly the same amount will the sleigh be able to fly.
Defying physics has rules, you know!

Of course, that's not the only problem.
The first group - the one going in the passenger compartment - needs as few packages as possible so that
Santa has some legroom left over. It doesn't matter how many packages are in either of the other two groups,
so long as all of the groups weigh the same.

Furthermore, Santa tells you, if there are multiple ways to arrange the packages such
that the fewest possible are in the first group, you need to choose the way where the first group
has the smallest quantum entanglement to reduce the chance of any "complications".
The quantum entanglement of a group of packages is the product of their weights, that is,
the value you get when you multiply their weights together.
Only consider quantum entanglement if the first group has the fewest possible number
of packages in it and all groups weigh the same amount.

For example, suppose you have ten packages with weights 1 through 5 and 7 through 11.
For this situation, the unique first groups, their quantum entanglements,
and a way to divide the remaining packages are as follows:

Group 1;             Group 2; Group 3
11 9       (QE= 99); 10 8 2;  7 5 4 3 1
10 9 1     (QE= 90); 11 7 2;  8 5 4 3
10 8 2     (QE=160); 11 9;    7 5 4 3 1
10 7 3     (QE=210); 11 9;    8 5 4 2 1
10 5 4 1   (QE=200); 11 9;    8 7 3 2
10 5 3 2   (QE=300); 11 9;    8 7 4 1
10 4 3 2 1 (QE=240); 11 9;    8 7 5
9 8 3      (QE=216); 11 7 2;  10 5 4 1
9 7 4      (QE=252); 11 8 1;  10 5 3 2
9 5 4 2    (QE=360); 11 8 1;  10 7 3
8 7 5      (QE=280); 11 9;    10 4 3 2 1
8 5 4 3    (QE=480); 11 9;    10 7 2 1
7 5 4 3 1  (QE=420); 11 9;    10 8 2

Of these, although 10 9 1 has the smallest quantum entanglement (90),
the configuration with only two packages, 11 9, in the passenger compartment gives
Santa the most legroom and wins. In this situation, the quantum entanglement for the
ideal configuration is therefore 99. Had there been two configurations with only two
packages in the first group, the one with the smaller quantum entanglement would be chosen.

What is the quantum entanglement of the first group of packages in the ideal configuration?
"""

# ========================================================
# Function to remove multiple elements from a list
def multi_remove(presents, elems):
    for i in elems:
        try:
            presents.remove(i)
        except ValueError:
            continue

    return presents

# ========================================================
# Function to split up list with equal sums
def split_list(presents):
    g2len = int(len(presents)/2)

    weight_goal = sum(presents)/2

    split_ok = False

    for n in range(1, g2len+1, 1):
        combos = combinations(presents, n)
        for g2 in combos:
            temp_pres = presents
            if sum(g2) != weight_goal: continue

            g3 = multi_remove(temp_pres, g2)
            if sum(g3) != weight_goal:
                continue
            else:
                #print 'Split:', g2, sum(g2), len(g2), g3, sum(g3), len(g3)
                split_ok = True

    return split_ok

# ========================================================
with open("files/input_d24.txt","r") as f:
    presents_orig = f.read().split('\n')[:-1]
presents_orig = [int(x) for x in presents_orig]

weight_goal = sum(presents_orig)/3

#print presents_orig
#print len(presents_orig), sum(presents_orig), weight_goal

from operator import mul # to multiply the list elements with reduce(mul, list, 1)
from itertools import combinations

qe_array = []
best_num = 10
for num in range(1, len(presents_orig)-1):
    combos = combinations(presents_orig, num)
    for i in combos:
        presents = presents_orig # copy over the original list

        if sum(i)!=weight_goal: continue # must be a third of the full weight
        presents = multi_remove(presents, i) # remove presents already in group 1
        if sum(presents)!=2*weight_goal: continue # remaning presents must be 2/3 of the full weight

        # Attempt an equal weight split
        if split_list(presents):
            qe = reduce(mul, i, 1)
            print 'Pass:', i, sum(i), len(i), qe
            qe_array.append(qe)
            if num <= best_num: best_num = num
            if num > best_num: break

print 'Part 1 Answer:', min(qe_array)

"""
--- Part Two ---

That's weird... the sleigh still isn't balancing.

"Ho ho ho", Santa muses to himself. "I forgot the trunk".

Balance the sleigh again, but this time, separate the packages into four groups instead of three.
The other constraints still apply.

Given the example packages above, this would be the new unique first groups,
their quantum entanglements, and one way to divide the remaining packages:


11 4    (QE=44); 10 5;   9 3 2 1; 8 7
10 5    (QE=50); 11 4;   9 3 2 1; 8 7
9 5 1   (QE=45); 11 4;   10 3 2;  8 7
9 4 2   (QE=72); 11 3 1; 10 5;    8 7
9 3 2 1 (QE=54); 11 4;   10 5;    8 7
8 7     (QE=56); 11 4;   10 5;    9 3 2 1

Of these, there are three arrangements that put the minimum (two) number of packages in the first group:
11 4, 10 5, and 8 7. Of these, 11 4 has the lowest quantum entanglement, and so it is selected.

Now, what is the quantum entanglement of the first group of packages in the ideal configuration?
"""

# ========================================================
# Function to split up list in three with equal sums
def split_list_3(presents, weight_goal):
    g2len = int(len(presents)/3)

    split_ok = False

    for n in range(1, g2len+1, 1):
        combos = combinations(presents, n)
        for g2 in combos:
            temp_pres = presents
            if sum(g2) != weight_goal: continue

            g3 = multi_remove(temp_pres, g2)
            if sum(g3) != 2*weight_goal:
                continue
            else:
                if split_list(g3): # Additional split
                    #print 'Split (1):', g2, sum(g2), len(g2)
                    split_ok = True

    return split_ok

# ========================================================
# Remaking original array
with open("files/input_d24.txt","r") as f:
    presents_orig = f.read().split('\n')[:-1]
presents_orig = [int(x) for x in presents_orig]

weight_goal = sum(presents_orig)/4

qe_array = []
best_num = 10
for num in range(1, len(presents_orig)-1):
    combos = combinations(presents_orig, num)
    for i in combos:
        presents = presents_orig # copy over the original list

        if sum(i)!=weight_goal: continue # must be a quarter of the full weight
        presents = multi_remove(presents, i) # remove presents already in group 1
        if sum(presents)!=3*weight_goal: continue # remaning presents must be 3/4 of the full weight

        # Attempt an equal three-way weight split
        if split_list_3(presents, weight_goal):
            qe = reduce(mul, i, 1)
            print 'Pass:', i, sum(i), len(i), qe
            if num <= best_num: best_num = num
            if num > best_num: break
            qe_array.append(qe)

print 'Part 2 Answer:', min(qe_array)