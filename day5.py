"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

# Using regular epressions
import re

# Read in the input file
f = open('files/input_d5.txt','r')

numnice = 0

for line in f:
    good = False

    # Search for bad strings
    t = re.search('ab|cd|pq|xy', line)
    if t:
        #print line, t.group()
        good = False
        continue

    # Search for double letters
    t = re.search(r'([a-z])\1', line)
    if t:
        #print line, t.group()
        good = True
    else:
        good = False
        continue

    # Count vowels
    t = re.findall('[aeiou]', line)
    if len(t)>=3:
        #print line, t
        good = True
    else:
        good = False
        continue

    if good:
        #print line
        numnice += 1


f.close()
print 'Part 1 Answer: ', numnice

# Part 2
"""
Realizing the error of his ways, Santa has switched to a better model of determining whether a
string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without
overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like
xyx, abcdefeghi (efe), or even aaa.
"""

# Read in the input file
f = open('files/input_d5.txt','r')

numnice = 0

for line in f:
    good = False

    # A pair of two letters at least twice without overlapping
    t = re.search(r'([a-z]{2})(.*)\1', line)
    if t:
        #print line, t.group()
        good = True
    else:
        good = False
        continue

    # One letter which repeats with one in between
    t = re.search(r'([a-z]).\1', line)
    if t:
        #print line, t.group()
        good = True
    else:
        good = False
        continue

    if good:
        #print line
        numnice += 1

f.close()
print 'Part 2 Answer: ', numnice