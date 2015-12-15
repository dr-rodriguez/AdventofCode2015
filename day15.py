"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients.
You make a list of the remaining ingredients you could use to finish the
recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the future.
The total score of a cookie can be found by adding up each of the properties
(negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
(because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880,
which happens to be the best score possible given these ingredients.
If any properties had produced a negative total, it would have instead become zero,
causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties,
what is the total score of the highest-scoring cookie you can make?
"""

# Read in the input file
f = open('files/input_d15.txt','r')

# Parse the file to grab all the ingredients and their properties
import re
regex = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (\d+), calories (\d+)'
ingredients = []
for line in f:
    name, cap, dur, fla, tex, cal = re.findall(regex, line.strip())[0]
    entry = {'name': name, 'cap': int(cap), 'dur': int(dur), 'fla': int(fla), 'tex': int(tex), 'cal': int(cal)}
    ingredients.append(entry)
    print entry
f.close()

# Loop over all possible ingredient combinations, a brute-force approach
score = 0
max_score = 0
for i in range(1,100):
    for j in range(1,100-i):
        for k in range(1,100-i-j):
            l = 100-i-j-k

            v1 = ingredients[0]['cap']*i + ingredients[1]['cap']*j + ingredients[2]['cap']*k + ingredients[3]['cap']*l
            v2 = ingredients[0]['dur']*i + ingredients[1]['dur']*j + ingredients[2]['dur']*k + ingredients[3]['dur']*l
            v3 = ingredients[0]['fla']*i + ingredients[1]['fla']*j + ingredients[2]['fla']*k + ingredients[3]['fla']*l
            v4 = ingredients[0]['tex']*i + ingredients[1]['tex']*j + ingredients[2]['tex']*k + ingredients[3]['tex']*l

            # For Part 2
            calories = ingredients[0]['cal']*i + ingredients[1]['cal']*j + ingredients[2]['cal']*k + ingredients[3]['cal']*l
            if calories!=500:
                continue

            if v1 < 0 or v2 < 0 or v3 < 0 or v4 < 0:
                score = 0
                continue

            score = v1 * v2 * v3 * v4

            if score > max_score:
                #print score, i, j, k, l
                max_score = score

print max_score

"""
--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has
exactly 500 calories per cookie (so they can use it as a meal replacement).
Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of
butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie
count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000,
the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of
the highest-scoring cookie you can make with a calorie total of 500?
"""