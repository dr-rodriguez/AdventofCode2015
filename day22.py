"""
--- Day 22: Wizard Simulator 20XX ---

Little Henry Case decides that defeating bosses with swords and stuff is boring.
Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns.
The player still goes first. Now, however, you don't get any equipment;
instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally.
However, since you do magic damage, your opponent's armor is ignored,
and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case)
would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast.
If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana,
but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately
deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

- Magic Missile costs 53 mana. It instantly does 4 damage.
- Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
- Shield costs 113 mana. It starts an effect that lasts for 6 turns.
While it is active, your armor is increased by 7.
- Poison costs 173 mana. It starts an effect that lasts for 6 turns.
At the start of each turn while it is active, it deals the boss 3 damage.
- Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way.
Effects apply at the start of both the player's turns and the boss' turns.
Effects are created with a timer (the number of turns they last); at the start of each turn,
after they apply any effect they have, their timer is decreased by one.
If this decreases the timer to zero, the effect ends.
You cannot cast a spell that would start an effect which is already active.
However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.


Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

You start with 50 hit points and 500 mana points.
The boss's actual stats are in your puzzle input.
What is the least amount of mana you can spend and still win the fight?
(Do not include mana recharge effects as "spending" negative mana.)
"""

# May take a while to run (~80sec on mine), but 1,000,000 iterations is good enough to get the answer

# ===================================================
# Player object to store all the relevant variables
class player:
    hp = 50
    mana = 500
    total_spent = 0
    armor = 0
    shield_on = 0
    poison_on = 0
    recharge_on = 0

    def do_damage(self, amount):
        global boss_hp
        boss_hp -= max(1, amount)

    def check_effect(self):
        if self.shield_on > 0:
            self.armor = 7
            self.shield_on -= 1
        else:
            self.armor = 0

        if self.poison_on > 0:
            self.do_damage(3)
            self.poison_on -= 1

        if self.recharge_on > 0:
            self.mana += 101
            self.recharge_on -= 1

    def check_mana(self, cost):
        if cost <= self.mana:
            self.mana -= cost
            self.total_spent += cost
            return True
        else:
            return False

    def cast_spell(self, spell_index):
        spell_cost = [53, 73, 113, 173, 229]

        spells_cast = set()
        spell_done = False
        #count = 0
        while not spell_done:

            # Magic Missile
            if spell_index==0:
                if self.check_mana(spell_cost[spell_index]):
                    self.do_damage(4)
                    spell_done = True

            # Drain
            if spell_index==1:
                if self.check_mana(spell_cost[spell_index]):
                    self.do_damage(2)
                    self.hp += 2
                    spell_done = True

            # Shield
            if spell_index==2:
                if self.check_mana(spell_cost[spell_index]):
                    if self.shield_on>0: continue # can't cast if already active
                    self.shield_on = 6
                    self.armor = 7
                    spell_done = True

            # Poison
            if spell_index==3:
                if self.check_mana(spell_cost[spell_index]):
                    if self.poison_on>0: continue
                    self.poison_on = 6
                    spell_done = True

            # Recharge
            if spell_index==4:
                if self.check_mana(spell_cost[spell_index]):
                    if self.recharge_on>0: continue
                    self.recharge_on = 5
                    spell_done = True

            # Attempt to cast next spell if not enough mana
            spells_cast.add(spell_index)
            if len(spells_cast)>=5: #all spells cast
                self.hp = 0
                #spell_done = True
                break

            new_spell = spell_index
            while new_spell in spells_cast:
                new_spell = randrange(0,5,1)
            spell_index = new_spell

            # spell_index = (spell_index + 1) % 5
            # count += 1
            # if count>5: # not enough mana for any spell, loose
            #     #print 'No mana'
            #     self.hp = 0
            #     spell_done = True
            #     break

    def take_damage(self, amount):
        self.hp -= max(1, amount - self.armor)

    def reset(self):
        self.hp = 50
        self.mana = 500
        self.armor = 0
        self.total_spent = 0
        self.shield_on = 0
        self.poison_on = 0
        self.recharge_on = 0

# ===================================================
# Function to simulate combat
def do_combat(p):
    global boss_hp
    boss_dmg = 8

    win = False
    while p.hp > 0:
        # Player turn
        p.check_effect()
        if boss_hp <= 0 and p.hp > 0: # player wins
            win = True
            break

        spell_index = randrange(0,5,1)
        p.cast_spell(spell_index)

        # Boss turn
        p.check_effect()
        if boss_hp <= 0 and p.hp > 0:
            win = True
            break
        p.take_damage(boss_dmg)

    return win

# ===================================================
p = player()

from random import randrange, seed
seed()

import time
start_time = time.time()

# Simulate combat
mana_spent = []
count = 0
while count<1000000:
    boss_hp = 55
    win = do_combat(p)
    if win:
        #print 'Victory!', boss_hp, p.hp, p.mana, p.total_spent
        mana_spent.append(p.total_spent)

    p.reset()

    count += 1

print ("--- %s seconds ---") % (time.time() - start_time)

#print mana_spent
if len(mana_spent)>0: print 'Part 1 Answer:', min(mana_spent)
# 953 best so far

"""
--- Part Two ---

On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point.
If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss,
what is the least amount of mana you can spend and still win the fight?
"""

# ===================================================
# Function to simulate combat, part 2
def do_combat2(p):
    global boss_hp
    boss_dmg = 8

    win = False
    while p.hp > 0:
        # Player turn
        p.hp -= 1
        if p.hp <= 0: # loose before any effects
            win = False
            break

        p.check_effect()
        if boss_hp <= 0 and p.hp > 0: # player wins
            win = True
            break

        spell_index = randrange(0,5,1)
        p.cast_spell(spell_index)

        # Boss turn
        p.check_effect()
        if boss_hp <= 0 and p.hp > 0:
            win = True
            break
        p.take_damage(boss_dmg)

    return win

start_time = time.time()

# Simulate combat
mana_spent = []
count = 0
while count<1000000:
    boss_hp = 55
    win = do_combat2(p)
    if win:
        #print 'Victory!', boss_hp, p.hp, p.mana, p.total_spent
        mana_spent.append(p.total_spent)

    p.reset()

    count += 1

print ("--- %s seconds ---") % (time.time() - start_time)

#print mana_spent
if len(mana_spent)>0: print 'Part 2 Answer:', min(mana_spent)
# 1289 best so far