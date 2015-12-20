"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door.
He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1.
Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents.
The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is 36000000.
"""

# Took some tips from the subreddit since my initial solution ran very very slowly

from math import sqrt

# Calculate how many presents to return
# This is **very** slow
def give_presents(house_num):
    presents = 0
    for i in range(1, house_num+1):
        if house_num % i == 0: presents += i*10
    return presents

# Factors function from StackOverflow
# This is much, much faster
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

# Brute-force approach, just calculate how many presents each house gets until I reach the number
# This can take a bit of time
house_num = 10
presents = 0
input_num = 36000000
while presents < input_num: #at least as many, don't need exactly the same number of presents
    house_num += 1
    #presents = give_presents(house_num)
    presents = 10*sum(factors(house_num)) # Much faster than give_presents()

print 'Part 1 Answer:', house_num, give_presents(house_num), 10*sum(factors(house_num))


"""
--- Part Two ---

The Elves decide they don't want to visit an infinite number of houses.
Instead, each Elf will stop after delivering presents to 50 houses.
To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the
house to get at least as many presents as the number in your puzzle input?
"""

house_num = 10
presents = 0
input_num = 36000000
while presents < input_num:
    house_num += 1
    # New presents calculation has an if statement to remove cases were more
    # than 50 houses have passed for each specific factor
    presents = 11*sum([x for x in factors(house_num) if house_num/x <= 50])

print 'Part 2 Answer:', house_num, 11*sum([x for x in factors(house_num) if house_num/x <= 50])