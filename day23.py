"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor.
It comes with instructions and an example program, but the computer itself seems to be malfunctioning.
She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions
(truly, it goes on to remind the reader, a state-of-the-art technology).
The registers are named a and b, can hold any non-negative integer, and begin with a value of 0.
The instructions are as follows:

hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction.
The offset is always written with a prefix + or - to indicate the direction of the jump
(forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction,
while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is finished executing?
"""

# Function to process the commands on the registry
def process_command(commands):
    global registry
    global ind

    comm = commands[ind]
    #print ind, comm, registry

    if comm[:3]=='inc':
        registry[comm[4]] += 1 # Increment
    elif comm[:3]=='tpl':
        registry[comm[4]] *= 3 # Triple
    elif comm[:3]=='hlf':
        registry[comm[4]] /= 2 # Half
    elif comm[:3]=='jmp': # Jump
        ind += int(comm[4:])-1
    elif comm[:3]=='jio': # Jump if one
        if registry[comm[4]] == 1: ind += int(comm[7:])-1 #-1 to cancel out the +1 that always gets done
    elif comm[:3]=='jie': # Even Jump
        if registry[comm[4]] % 2 == 0: ind += int(comm[7:])-1

    ind += 1
    return ind

# Read in the input file
with open("files/input_d23.txt", 'r') as f:
    commands = f.read().split('\n')[:-1]

registry = {'a': 0, 'b': 0}

ind = 0
while ind >= 0 and ind<len(commands):
    ind = process_command(commands)

print 'Part 1 Answer:', registry['b']

"""
--- Part Two ---

The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer.
Definitely not to distract you,
what is the value in register b after the program is finished executing if register a starts as 1 instead?
"""

registry = {'a': 1, 'b': 0}

ind = 0
while ind >= 0 and ind<len(commands):
    ind = process_command(commands)

print 'Part 2 Answer:', registry['b']