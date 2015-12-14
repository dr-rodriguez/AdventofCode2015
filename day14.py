"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest
occasionally to recover their energy. Santa would like to know which of his
reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all),
 and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds,
Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second,
Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km.
On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when
Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at
1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation,
Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input),
after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

import re
import numpy as np

# Process a reindeer for the input time
def process(velocity, vel_t, rest_t, proctime):
    dist = 0
    moving = True

    while proctime > 0:
        if moving:
            if vel_t < proctime:
                dist += velocity * vel_t
                proctime -= vel_t
                moving = False
            else: # remaining time is less than velocity time
                dist += velocity * proctime
                proctime = 0

        if not moving:
            if rest_t < proctime:
                proctime -= rest_t
                moving = True
            else:
                proctime = 0

    return dist

proctime = 2503

# Read in file
f = open('files/input_d14.txt','r')

# Parse file and process the reindeer
for line in f:
    regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    name, velocity, vel_t, rest_t = re.findall(regex, line)[0]
    print name, process(int(velocity), int(vel_t), int(rest_t), proctime)

f.close()

"""
--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead.
(If there are multiple reindeer tied for the lead, they each get one point.)
He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point.
He stays in the lead until several seconds into Comet's second burst: after the 140th second,
Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead
for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion,
only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds,
how many points does the winning reindeer have?
"""

f = open('files/input_d14.txt','r')

# Parse file and process the reindeer. The dictionary will store distance, score, moving status, etc
reindeer = []
for line in f:
    regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
    name, velocity, vel_t, rest_t = re.findall(regex, line)[0]
    entry = {'name': name, 'vel': int(velocity), 'vel_t': int(vel_t), \
             'rest_t': int(rest_t), 'dist':0, 'score': 0, 'move': True, 'remain': int(vel_t)}
    reindeer.append(entry)

f.close()

print 'Part 2'
proctime = 2503

# Simulate each second and check distances
while proctime>=0:
    distlist = []
    for entry in reindeer:
        if entry['move']:
            entry['dist'] = entry['dist'] + entry['vel']
            entry['remain'] = entry['remain'] - 1 # remaing time in phase
            if entry['remain'] == 0: # go get rest
                entry['move'] = False
                entry['remain'] = entry['rest_t']
        else:
            entry['remain'] = entry['remain'] - 1
            if entry['remain'] == 0: # go fly again
                entry['move'] = True
                entry['remain'] = entry['vel_t']

        distlist.append(entry['dist'])

    # Check max distance and award score
    distlist = np.array(distlist)
    ind = np.where(distlist == max(distlist))

    for i in ind[0]:
        reindeer[i]['score'] = reindeer[i]['score'] + 1
        #print proctime, i, reindeer[i]['name'], reindeer[i]['score']

    proctime -= 1

# Grab the winner
score = []
for entry in reindeer:
    print entry['name'], entry['score'], entry['dist']
    score.append(entry['score'])

print max(score)