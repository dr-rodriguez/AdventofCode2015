"""
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically
forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.
"""

import hashlib

# My key
key = 'iwrupvqb'

count = 1
answer = 0
while answer == 0:
    newkey = key + str(count)
    val = hashlib.md5(newkey).hexdigest()
    #print newkey, val

    # Check if first 5 are zeros (or 6 for part 2)
    #if(val[:6]=='000000'):
    if(val[:5]=='00000'):
        answer = count
        print newkey, val
        print 'Answer: ', count

    count += 1

