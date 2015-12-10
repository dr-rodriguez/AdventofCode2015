"""
Today, the Elves are playing a game called look-and-say. They take turns making sequences by
reading aloud the previous sequence and using that reading as the next sequence. For example,
211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step.
For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3)
followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 1321131112.
"""

# Function to count the digits
def lookandsee(val):

    maxlen = len(valstr)
    count = 1
    answer = ''
    for i in range(maxlen):
        currchar = valstr[i]
        if i+1 < maxlen:
            nextchar = valstr[i+1]
        else:
            nextchar = 0

        if currchar == nextchar:
            count += 1
        else:
            answer = answer + str(count) + currchar
            count = 1

    return answer

# Run with my input
my_input = '1321131112'

for i in range(40):
    #old_input = my_input
    my_input = lookandsee(my_input)
    #print float(len(my_input))/float(len(str(old_input))) # Just for fun, approaches Conway's constant
    #print my_input


print 'Part 1 Answer: ', len(my_input)

# Part 2

"""
Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result
"""

my_input = '1321131112'

# This one takes an incredibly long time, not sure how to optimize it
for i in range(50):
    print i # To check on progress
    my_input = lookandsee(my_input)

print 'Part 2 Answer: ', len(my_input)