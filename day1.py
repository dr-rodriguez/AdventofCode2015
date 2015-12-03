"""
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
"""

# Read in input_d1p1.txt
f = open('files/input_d1p1.txt', 'r')
floorcommands = f.read()
f.close()

answer = 0
for value in floorcommands:
    if(value == '('): answer += 1
    if(value == ')'): answer -= 1

print answer

"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1).
The first character in the instructions has position 1, the second character has position 2, and so on.
"""

answer = 0
for index in range(len(floorcommands)):
    value = floorcommands[index]
    if(value == '('): answer += 1
    if(value == ')'): answer -= 1
    if(answer<0):
        print index+1, answer
        break