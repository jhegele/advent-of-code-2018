# comments on differences from part 1, much of this is replicated
from collections import Counter

class Cart(object):

    # we add an id property to our class so that we can easily
    # differentiate between our carts.
    def __init__(self, id, c, p):
        if c == '^':
            self.dir = 'U'
        elif c == 'v':
            self.dir = 'D'
        elif c == '<':
            self.dir = 'L'
        else:
            self.dir = 'R'
        self.pos = p
        self.int_ct = 0
        # also add a crashed indicator which allows us to track what
        # has crashed without actually messing with our list of carts
        self.crashed = False
        self.id = id

    def move(self, t):
        # first we adjust the position based on the direction we're
        # facing. we can do this naively because we will turn the
        # cart after repositioning (so the next move is always valid)
        x, y = self.pos
        if self.dir == 'U':
            self.pos = (x, y - 1)
        elif self.dir == 'D':
            self.pos = (x, y + 1)
        elif self.dir == 'L':
            self.pos = (x - 1, y)
        else:
            self.pos = (x + 1, y)
        # we need to evaluate the track type at the new position and, if
        # necessary, we adjust the position (i.e. if we're at a curve or
        # intersection, we need to turn so that our next move will be
        # valid)
        tt = t[self.pos]
        if tt == '\\':
            d = 'UDLR'
            m = 'LRUD'
            self.dir = m[d.index(self.dir)]
        if tt == '/':
            d = 'UDLR'
            m = 'RLDU'
            self.dir = m[d.index(self.dir)]
        if tt == '+':
            self.int_ct += 1
            # LSR
            if self.int_ct % 3 == 1:
                d = 'UDLR'
                m = 'LRDU'
                self.dir = m[d.index(self.dir)]
            if self.int_ct % 3 == 0:
                d = 'UDLR'
                m = 'RLUD'
                self.dir = m[d.index(self.dir)]
        return self.pos

with open('./inputs/parts1-2.txt') as puzzle_input:
    i = [line.replace('\n', '') for line in puzzle_input.readlines()]

tracks = {}
carts = []
cid = 1
for y in range(0, len(i)):
    for x in range(0, len(i[y])):
        c = i[y][x] 
        if c != ' ':
            if c in '<>v^':
                ct = Cart(cid, c, (x, y))
                carts.append(ct)
                cid += 1
                if ct.dir in '<>':
                    t = '-'
                else:
                    t = '|'
                tracks[(x, y)] = t
            else:
                tracks[(x, y)] = c

while True:
    carts.sort(key=lambda k: (k.pos[1], k.pos[0]))
    # we need to loop through our carts each time
    for c in carts:
        # we only want to move carts that have NOT crashed
        if not c.crashed:
            new_pos = c.move(tracks)
            # after we move a cart, we need to check for collisions. if
            # there are collisions, we set BOTH carts crashed property
            # to true.
            carts_at_new_pos = [ct for ct in carts if ct.pos == new_pos and not ct.crashed]
            if len(carts_at_new_pos) > 1:
                for ct in carts_at_new_pos:
                    ct.crashed = True
    # check the carts that have not crashed and, if we only have one
    # remaining then we're done.
    active_carts = [ct for ct in carts if not ct.crashed]
    if len(active_carts) == 1:
        print('Last remaining cart at {}'.format(active_carts[0].pos))
        break
    
