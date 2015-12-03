"""
The elves are running low on wrapping paper, and so they need to submit an order for more.
They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present: the area of the smallest side.
"""

print 'Part 1'

# Read in input
f = open('files/input_d2p1.txt', 'r')

# Read each line and calculate surface area + smallest side area
answer = 0
for line in f:
    elems = line.split('x')
    l = float(elems[0])
    w = float(elems[1])
    h = float(elems[2])
    a1 = l*w
    a2 = w*h
    a3 = h*l
    atot = 2 * (a1 + a2 + a3)
    mina = min(a1,a2,a3)

    #print l, w, h, a1, a2, a3, mina, atot


    answer = answer + atot+ mina

print answer

f.close()

"""
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about
the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter
of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for
the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
"""

print 'Part 2'

# Re-read in input
f = open('files/input_d2p1.txt', 'r')

# Read each line and calculate smallest perimeter + volume
answer = 0
for line in f:
    elems = line.split('x')
    l = float(elems[0])
    w = float(elems[1])
    h = float(elems[2])
    vol = l*w*h
    p1 = 2*(l+w)
    p2 = 2*(w+h)
    p3 = 2*(l+h)
    minp = min(p1,p2,p3)

    #print line, p1, p2, p3, vol, minp

    answer = answer + minp + vol


print answer

f.close()