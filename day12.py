"""
Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}),
numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
"""

# Although it may want us to import as a JSON file, it sounds far easier to do as a simple text file and regex
import re

f = open('files/input_d12.txt','r')
alltext = f.read()
f.close()

# Match any number of decimal digits and include the - sign if any
t = re.findall('-?\d+',alltext)
t = [int(s) for s in t]
#print t
print 'Part 1 Answer: ', sum(t)


# Part 2
"""
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red".
Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""

# This time I have to parse it with json
# Got hints from the subreddit

import json
data = json.loads(alltext)

# Grab json elements
def sum_data(data):
    if type(data) == type(dict()): # If this is a dictionary, check keys and process
        #print 'Dictionary:', data

        # Ignore anything with 'red' values. Can comment this out to recover the answer to part 1
        if "red" in data.values(): return 0

        return sum(map(sum_data, data.values())) # for each value, call the function and sum up the resulting list

    if type(data) == type([]): # If arrays or lists, process call the function for each element in the list
        #print 'Array:', data
        return sum(map(sum_data, data))

    if type(data) == type(0): # If a number, return it to be added
        #print 'Number:', data
        return data

    return 0

print 'Part 2 Answer:', sum_data(data)
