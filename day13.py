"""
In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along! This year, you resolve, will be different.
You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would
increase or decrease if they were to find themselves sitting next to each other person.
You have a circular table that will be just big enough to fit everyone comfortably,
and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned,
and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much),
but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54).
Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41).
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario,
you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""

# Apparently, using itertools and permutations will make this easier as it seems
# I may have just ended up writing my own permutation code

import random

# Generate list of participant names and pairs
def gen_lists(alltext):
    global all_names
    global all_pairs
    for line in alltext:
        elems = line.split()
        name1 = elems[0]
        name2 = elems[-1][:-1]
        happy = int(elems[3])
        sign = elems[2]
        if sign=='lose': happy = -1*happy

        if name1 not in all_names: all_names.append(name1)
        if name2 not in all_names: all_names.append(name2)

        pair_dict = dict([('p1',name1),('p2',name2),('happy',happy)])
        all_pairs.append(pair_dict)

# Set the table
def make_table():
    global all_names
    global all_pairs

    # Shuffle lists
    random.shuffle(all_names)
    random.shuffle(all_pairs)

    # Grab first participant and remove from list
    guest1 = all_names[0]
    firstguest = guest1
    all_names.remove(guest1)

    # Guests already seated
    seated = []
    seated.append(guest1)
    final_table = []

    # Repeat until all participants are eliminated
    while len(all_names)>1:
        entry = find_pair(guest1, seated)

        # Add the new guest to the table
        final_table.append(entry)
        all_pairs.remove(entry)

        if guest1==entry['p1']:
            guest2 = entry['p2']
        else:
            guest2 = entry['p1']

        # Find reverse pair and add it
        entry = reverse_pair(entry)
        final_table.append(entry)

        all_pairs.remove(entry)
        all_names.remove(guest2)
        seated.append(guest2)

        guest1 = guest2


    # Penultimate entry
    entry = find_pair(guest1, seated)
    all_pairs.remove(entry)
    final_table.append(entry)
    entry = reverse_pair(entry)
    final_table.append(entry)

    # Final entry with original guest
    entry = find_pair(firstguest, seated)
    final_table.append(entry)
    entry = reverse_pair(entry)
    final_table.append(entry)

    return final_table

# Find match in pair
def find_pair(guest, seated):
    global all_pairs
    for entry in all_pairs:

        # If no match in pairs, continue
        if guest not in entry.values(): continue

        if guest==entry['p1']:
            guest2 = entry['p2']
        else:
            guest2 = entry['p1']

        # If guest is already seated at table, not a valid choice
        if guest2 in seated: continue

        return entry

# Find the other part of the pair which needs to be included
def reverse_pair(entry0):
    global all_pairs
    for entry in all_pairs:

        # Don't match the same entry
        if (entry0['p1']==entry['p1']) or (entry0['p2']==entry['p2']): continue

        # Match the reverse
        if (entry0['p1']==entry['p2']) and (entry0['p2']==entry['p1']):
            return entry


# Read in input
f = open('files/input_d13.txt','r')
alltext = f.read().split('\n')[:-1]
f.close()

random.seed()


happysum = 0
maxhappy = 733-1
count = 0

# Loop until max happy
while happysum < maxhappy:
    all_names = [] # very important to reset the names and pairs variables
    all_pairs = []

    gen_lists(alltext)
    final_table = make_table()

    # Tally up happiness values
    happysum = 0
    for entry in final_table:
        happysum += entry['happy']

    if happysum >= maxhappy:
        maxhappy = happysum
        print happysum, 'for', final_table

    # Hard break if exceeds counts
    count += 1
    if count>10000:
        print 'Max counts reached'
        break

print 'Part 1 Answer:', maxhappy
print 'Part 1 Table:', final_table


"""
--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself.
At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't
really go up or down regardless of who you sit next to. You assume everyone else would be
just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""

def add_name(new_name):
    global all_names
    global all_pairs
    # Add myself
    for name in all_names:
        entry = dict([('p1',new_name),('p2',name),('happy',0)])
        all_pairs.append(entry)
        entry = dict([('p2',new_name),('p1',name),('happy',0)])
        all_pairs.append(entry)

    all_names.append(new_name)

happysum = 0
maxhappy = 725-1
count = 0
# Loop until max happy
while happysum < maxhappy:
    all_names = [] # very important to reset the names and pairs variables
    all_pairs = []
    gen_lists(alltext)

    add_name('Strakul') #add myself to the lists

    final_table = make_table()

    # Tally up happiness values
    happysum = 0
    for entry in final_table:
        happysum += entry['happy']

    if happysum >= maxhappy:
        maxhappy = happysum
        print happysum, 'for', final_table

    # Hard break if exceeds counts
    count += 1
    if count>10000:
        print 'Max counts reached'
        break

print 'Part 2 Answer:', maxhappy
print 'Part 2 Table:', final_table

# ===========================================================================================

# For fun, a re-attempt using itertools and permutations after looking through the subreddit
# This is much faster and much more compact!

def make_pair_list(alltext):
    global all_names
    global all_pairs
    for line in alltext:
        elems = line.split()
        name1 = elems[0]
        name2 = elems[-1][:-1]
        happy = int(elems[3])
        sign = elems[2]
        if sign=='lose': happy = -1*happy

        all_names.add(name1)
        all_pairs[name1+name2] = happy

def compute(person):
    L = len(all_names)
    t = 0
    for i in range(L):
        t += all_pairs[person[i]+person[i-1]]
        t += all_pairs[person[i]+person[(i+1) % L]] # modulo to go around the table
    return t

from itertools import permutations
all_names = set() # now a set rather than list
all_pairs = {} # now a dictionary rather than list
make_pair_list(alltext)
print 'Part 1 Answer:', max([compute(person) for person in permutations(all_names)])
#print all_names
#print all_pairs

# Add myself to the set and the pairs
all_names.add('me')
for person in all_names:
    all_pairs[person+'me'] = 0
    all_pairs['me'+person] = 0

print 'Part 2 Answer:', max([compute(person) for person in permutations(all_names)])