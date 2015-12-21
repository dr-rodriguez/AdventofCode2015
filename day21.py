"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas.
It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop.
He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking.
The player always goes first. Each attack reduces the opponent's hit points by at least 1.
The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.
An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the
defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor
score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero.
They can be increased by buying items in exchange for gold.
You start with no items and have as much gold as you need.
Your total damage or armor is equal to the sum of those stats from all of your items.
You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one.
You can buy 0-2 rings (at most one for each hand). You must use any items you buy.
The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor,
and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input.
What is the least amount of gold you can spend and still win the fight?
"""

"""
My input
Boss:
Hit Points: 100
Damage: 8
Armor: 2
"""

# ===================================================
# Player object to store all the relevant variables
class player:
    hp = 100
    damage = 0
    armor = 0

    def take_damage(self, amount):
        self.hp -= max(1, amount - self.armor)

    def reset(self):
        self.hp = 100
        self.damage = 0
        self.armor = 0

# ===================================================
# Function to simulate combat
def do_combat(p):
    boss_hp = 100
    boss_dmg = 8
    boss_def = 2

    win = False
    while p.hp > 0:
        boss_hp -= max(1, p.damage - boss_def)

        if boss_hp <=0: # player wins
            win = True
            break

        p.take_damage(boss_dmg)

    return win

# ===================================================
from itertools import product

# Initializing the arrays
weap_cost = [0, 8, 10, 25, 40, 74]
weap_dmg = [0, 4, 5, 6, 7, 8]
armor_cost = [0, 13, 31, 53, 75, 102]
armor_def = [0, 1, 2, 3, 4, 5]
ring_cost = [0, 25, 50, 100, 20, 40, 80]
ring_dmg = [0, 1, 2, 3, 0, 0, 0]
ring_def = [0, 0, 0, 0, 1, 2, 3]

p = player()

amount_spent = []
combos = product(range(6), repeat=4)
for i in combos:
    if i[2]==i[3] and (i[2]!=0 or i[3]!=0): continue # can't have same ring twice
    if i[0]==0: continue # need a weapon

    p.damage = weap_dmg[i[0]] + ring_dmg[i[2]] + ring_dmg[i[3]]
    p.armor = armor_def[i[1]] + ring_def[i[2]] + ring_def[i[3]]
    cost = weap_cost[i[0]] + armor_cost[i[1]] + ring_cost[i[2]] + ring_cost[i[3]]

    # Do combat and record wins
    win = do_combat(p)
    if win: amount_spent.append(cost)

    p.reset() # Reset HP and other parameters

# Grab the minimum amount spent
print 'Part 1 Answer:', min(amount_spent)

"""
--- Part Two ---

Turns out the shopkeeper is working with the boss, and can persuade you
to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?
"""

amount_spent = []
combos = product(range(6), repeat=4)
for i in combos:
    if i[2]==i[3] and (i[2]!=0 or i[3]!=0): continue # can't have same ring twice
    if i[0]==0: continue # need a weapon

    p.damage = weap_dmg[i[0]] + ring_dmg[i[2]] + ring_dmg[i[3]]
    p.armor = armor_def[i[1]] + ring_def[i[2]] + ring_def[i[3]]
    cost = weap_cost[i[0]] + armor_cost[i[1]] + ring_cost[i[2]] + ring_cost[i[3]]

    # Do combat and record LOSSES
    win = do_combat(p)
    if not win: amount_spent.append(cost)

    p.reset() # Reset HP and other parameters

# Grab the maximum amount spent
print 'Part 2 Answer:', max(amount_spent)