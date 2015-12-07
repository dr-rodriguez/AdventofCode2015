"""
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately,
little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a
signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until
all of its inputs have a signal.

The included instructions booklet describe how to connect the parts together: x AND y -> z means to connect
wires x and y to an AND gate, and then connect its output to wire z.
"""

# Had to check the solutions to know how to work this one
# This one in particular helped out a lot:
# https://www.reddit.com/r/adventofcode/comments/3vr4m4/day_7_solutions/cxq47mv

# =============================================================================

# Main code to process the file (manually removed an extra line at end)
def process(line, wires):
    w_in, w_out = line.strip().split(' -> ')

    # Parse the input wires to have proper commands
    w_in = w_in.replace('RSHIFT', '>>').replace('LSHIFT', '<<').replace('AND','&').replace('OR','|').replace('NOT','0xffff ^ ')

    # Fixing reserved keywords
    w_in = w_in.replace('is','is1').replace('in','in1').replace('as','as1').replace('if','if1')
    w_out = w_out.replace('is','is1').replace('in','in1').replace('as','as1').replace('if','if1')

    # Attempt to execute the command. Add it to wires dictionary
    try:
        exec('%s = (%s) & 0xffff' % (w_out, w_in), {}, wires)
        return True
    except NameError:
        return False

# =============================================================================

# Read in the input file
f = open('files/input_d7.txt','r')

alltext = f.read().split('\n')
wires = {}

# Loop through all the text. Results are saved to wires using process() but the text is shortened
# whenever a valid signal is processed. Once all signals are processed, the while loop ends.
while len(alltext) > 0:
    alltext = [s for s in alltext if not process(s, wires)]

print wires
val = wires['a']
print 'Part 1 Answer: ', val

"""
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
What new signal is ultimately provided to wire a?
"""

# Part 2

# Resetting everything
wires = {}
f.seek(0)
alltext = f.read().split('\n')

# Making sure b gets only the saved value and no other
for elem in alltext:
    if elem[-4:] == '-> b': alltext.remove(elem)

alltext.append('%s -> b' % val)

# Process the new signals
while len(alltext) > 0:
    alltext = [s for s in alltext if not process(s, wires)]

print wires
print 'Part 2 Answer:', wires['a']


f.close()