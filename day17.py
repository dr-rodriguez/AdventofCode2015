"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time.
To fit it all into your refrigerator, you'll need to move it into smaller containers.
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

from itertools import combinations

def grabandtest(num):
    global containers

    count = 0
    for i in combinations(containers, num):
        temp_sum = sum(i)
        if temp_sum == 150:
            #print 'Good:', i
            count += 1

    return count

f = open('files/input_d17.txt','r')
containers = []
for line in f:
    elem = int(line.strip())
    containers.append(elem)
f.close()
print containers

answer = 0
for j in range(1, len(containers)):
    answer += grabandtest(j)

print 'Part 1 Answer:', answer

"""
--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives!
The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog.
How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two.
There were three ways to use that many containers, and so the answer there would be 3.
"""

def grabandtest2(num):
    global containers

    minreached = False
    count = 0
    for i in combinations(containers, num):
        temp_sum = sum(i)
        if temp_sum == 150:
            #print 'Good:', i, 'for num=', num
            count += 1
            minreached = True

    if minreached:
        return count
    else:
        return 0

answer = 0
num = 1
while answer==0:
    answer = grabandtest2(num)
    num += 1

print 'Part 2 Answer:', answer