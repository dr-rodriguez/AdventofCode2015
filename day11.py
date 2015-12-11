"""
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires,
Santa has devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons),
so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next
letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters,
  like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij)
  but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?
"""

import re # to use regular expressions

# ==============================================================================
# Function to test string
def test_str(strinput):

    # Check for i, o, or l
    t = re.findall('[iol]', strinput)
    if len(t)>0:
        #print strinput, ' contains i o or l'
        return False

    # Check for two pairs of letters
    check1 = False
    t = re.search(r'([a-z])\1(.*)([a-z])\3',strinput)
    if t:
        #print strinput, ' passes check for grouping: ', t.group()
        check1 = True

    # Check for an increasing straight of 3 letters
    check2 = False
    for i in range(len(strinput)-2):
        num1 = ord(strinput[i])
        num2 = ord(strinput[i+1])
        num3 = ord(strinput[i+2])
        if (num2 == num1 + 1) and (num3 == num2 + 1):
            #print strinput, ' passes check for increasing string'
            check2 = True

    if check1 and check2:
        print strinput, ' passes all checks'
        return True
    else:
        return False

# ==============================================================================

# Function to increment string. This will recursively call itself to properly increment
def incr_str(s):
    temp = ""
    if ord(s[len(s)-1]) >= 122: # check last letter, if z, the last letter is a and increment the prior string
        temp += incr_str(s[:len(s)-1]) + "a"
    else:
        val = s[:len(s)-1] + chr(ord(s[len(s)-1])+1) # return everything up to the last letter and the incremented last letter
        return val
    return temp

# ==============================================================================

my_input = 'hxbxwxba'
#my_input = 'abcdefgz'

while not test_str(my_input):
    my_input = incr_str(my_input)

print 'Part 1 Answer: ', my_input

# Part 2

"""
Santa's password expired again. What's the next one?
"""

count = 0
while (not test_str(my_input)) or count < 1:
    my_input = incr_str(my_input)
    if test_str(my_input): count += 1

print 'Part 2 Answer: ', my_input