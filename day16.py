"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card.
However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue
(which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as
luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine!
Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific
compounds in a given sample, as well as how many distinct kinds of those compounds there are.
According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these.
You put the wrapping from the gift into the MFCSAM.

It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue.
Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
"""

# Read in the file
f = open('files/input_d16.txt','r')

import re

# Dictionary to match
mfcsam = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, \
          'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
print mfcsam

# Loop through the file and eliminate those that don't match the specified criteria
# Sue 1: children: 1, cars: 8, vizslas: 7
regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
answer = 0
for line in f:
    num, crit1, val1, crit2, val2, crit3, val3 = re.findall(regex, line.strip())[0]
    val1, val2, val3 = int(val1), int(val2), int(val3)
    #print num, crit1, val1, crit2, val2, crit3, val3
    #print crit1, mfcsam[crit1], val1

    if mfcsam[crit1] != val1: continue
    if mfcsam[crit2] != val2: continue
    if mfcsam[crit3] != val3: continue

    print num, crit1, val1, crit2, val2, crit3, val3

    answer = num

print 'Part 1 Answer: ', answer

"""
--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye.
Apparently, it has an outdated retroencabulator,
and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many
(due to the unpredictable nuclear decay of cat dander and tree pollen),
while the pomeranians and goldfish readings indicate that there are fewer than that many
(due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""

f.seek(0)

def specialcheck(crit, val):
    global mfcsam

    if crit=='trees' or crit=='cats':
        if val > mfcsam[crit]: return True
    elif crit=='pomeranians' or crit=='goldfish':
        if val < mfcsam[crit]: return True
    else:
        if mfcsam[crit] == val: return True

    return False

answer = 0
for line in f:
    num, crit1, val1, crit2, val2, crit3, val3 = re.findall(regex, line.strip())[0]
    val1, val2, val3 = int(val1), int(val2), int(val3)
    #print num, crit1, val1, crit2, val2, crit3, val3
    #print crit1, mfcsam[crit1], val1

    if specialcheck(crit1, val1) and specialcheck(crit2, val2) and specialcheck(crit3, val3):
        print num, crit1, val1, crit2, val2, crit3, val3
        answer = num

print 'Part 2 Answer:', answer
f.close()