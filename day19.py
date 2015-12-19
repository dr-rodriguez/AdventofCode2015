"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology;
Rudolph is going to need custom-made medicine.
Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant,
capable of constructing any Red-Nosed Reindeer molecule you need.
It works by starting with some input molecule and then doing a series of replacements,
one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used.
Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, the following molecules could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice)
after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules
(over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O,
the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom,
the medicine molecule for which you need to calibrate the machine.
How many distinct molecules can be created after all the different
ways you can do one replacement on the medicine molecule?
"""

# Manually edited file to eliminate input string from there
input_string = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

# Read and parse the input
import re
f = open('files/input_d19.txt','r')
regex = r'(\w+) => (\w+)'
inrep = []
outrep = []
in_unique = set()
for line in f:
    e1, e2 = re.findall(regex, line.strip())[0]
    inrep.append(e1)
    outrep.append(e2)
    in_unique.add(e1)
f.close()

# Only ONE step is required for calibration
out_unique = set()
for j in range(len(inrep)):
    elem = inrep[j]
    t = re.finditer(inrep[j], input_string)
    for i in t:
        newstring = input_string[:i.start()] + outrep[j] + input_string[i.end():]
        out_unique.add(newstring)

print 'Part 1 Answer:', len(out_unique)

"""
--- Part Two ---

Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e,
and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH
If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH
So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine?
Given the available replacements and the medicine molecule in your puzzle input,
what is the fewest number of steps to go from e to the medicine molecule?
"""

# For this, lets work backwards until we get e
# This sounds like it could be more efficient with itertools, but not sure how to frame that
# Instead, will use a brute-force approach and just iteration a ton of times until I get the best answer

# In the end, had to use the guide and hint at https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
# I still include my original code as it does give a result, just not necessarily the best result and it takes a long time

def make_replacement(rep_str, outrep, input_str):

    t = re.finditer(rep_str, input_str)
    t2 = re.findall(rep_str, input_str)

    # If no matches, exit
    if len(t2)==0:
        return input_str

    # Select a random instance to replace
    ind = random.randint(0, len(t2)-1)
    count = 0

    for i in t:
        if count == ind: newstring = input_str[:i.start()] + outrep + input_str[i.end():]
        count += 1

    return newstring


# Create an index array that will be used for shuffling
index_array = range(len(inrep))

import random
random.seed()

def reduce_medicine(newstring):
    global outrep
    global inrep
    global index_array
    count = 0

    while count<10000:
        count += 1
        random.shuffle(index_array)
        ind = index_array[0]
        rep_str = outrep[ind]
        out_str = inrep[ind]
        newstring = make_replacement(rep_str, out_str, newstring)

        if newstring=='e':
            #print 'e reached:', count
            return count

    return 9999


bestanswer = 195-1
answer = 9999
count = 0

while answer>bestanswer:
    newstring = input_string
    answer = reduce_medicine(newstring)
    if answer != 9999 and answer<bestanswer:
        bestanswer = answer

    count += 1
    if count==10000:
        print 'Max counts reached, may not be correct'
        bestanswer += 1
        break

print 'Part 2 Answer:', bestanswer

# With the hints and guide of https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
regex = r'Rn|Ar|Y|Ca|Si|Th|B|F|C|P|Mg|Ti|Al' # all elements
#print re.sub(regex, '', input_string) # check that the regex grabs all the elements
str_len = len(re.findall(regex, input_string))
len1 = len(re.findall(r'Rn|Ar', input_string))
len2 = len(re.findall(r'Y', input_string))
print 'Part 2 Answer, better method:', str_len - len1 - 2*len2 - 1