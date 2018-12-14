from collections import Counter

# create a cart object so that it can track the state of the card. we need
# to keep track of where the cart is and which direction it's facing. with
# that info, we can easily move it around our track.
class Cart(object):

    # take the character representing the cart and the position (x, y) as
    # our initial inputs
    def __init__(self, c, p):
        # use the character to determine which way the cart is moving to
        # start
        if c == '^':
            self.dir = 'U'
        elif c == 'v':
            self.dir = 'D'
        elif c == '<':
            self.dir = 'L'
        else:
            self.dir = 'R'
        self.pos = p
        # we also need to track the number of intersections we've crossed
        # in order to turn the proper direction at each intersection
        self.int_ct = 0

    # this method moves the cart one spot. the approach we want to use is
    # to move the cart, then adjust the orientation if necessary. in this
    # way, we can avoid examining the track around the cart as we know
    # that it's always facing the right way for the next move.
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
            # based on the type of track, we can map the new orientation.
            # we need to account for each variation depending on which
            # direction the cart is traveling.
            d = 'UDLR'
            m = 'LRUD'
            self.dir = m[d.index(self.dir)]
        if tt == '/':
            d = 'UDLR'
            m = 'RLDU'
            self.dir = m[d.index(self.dir)]
        if tt == '+':
            # if we've hit an intersection, we turn based on the number
            # of intersections we've previously hit.
            self.int_ct += 1
            if self.int_ct % 3 == 1:
                d = 'UDLR'
                m = 'LRDU'
                self.dir = m[d.index(self.dir)]
            if self.int_ct % 3 == 0:
                d = 'UDLR'
                m = 'RLUD'
                self.dir = m[d.index(self.dir)]

# get puzzle inputs as lines
with open('./inputs/test3.txt') as puzzle_input:
    i = [line.replace('\n', '') for line in puzzle_input.readlines()]

# we are going to store the track layout as a dictionary where the key is
# the coordinates and the value is the actual track character from the
# input. this allows us to lookup the track at any point very easily. we
# will also store all of the carts as a list so that it's easy to update
# all of them using a loop.
tracks = {}
carts = []
# we need to parse the puzzle input line-by-line and character-by-
# character. we only store actual characters, no whitespace.
for y in range(0, len(i)):
    for x in range(0, len(i[y])):
        c = i[y][x] 
        # skip any whitespace
        if c != ' ':
            # if the character is a cart, initialize a cart object
            if c in '<>v^':
                ct = Cart(c, (x, y))
                carts.append(ct)
                # based on the diretion our cart is facing, we can
                # also assume the track type underneath it
                if ct.dir in 'LR':
                    t = '-'
                else:
                    t = '|'
                tracks[(x, y)] = t
            else:
                tracks[(x, y)] = c

ct = 0
# loop until we're done, then we'll break the loop
while True:
    ct += 1
    # initialize an answer variable that we can later use to break
    # the loop.
    ans = ''
    # this really messed me up because i totally missed that the carts
    # move in a determined pattern. here we sort our list of carts so 
    # that the move in the proper sequence.
    carts.sort(key=lambda k: (k.pos[1], k.pos[0]))
    for c in carts:
        c.move(tracks)
        # after every move we need to check for collisions. if there
        # is no collision, continue, otherwise break our loops and
        # print the answer.
        c_pos = [c.pos for c in carts]
        c = Counter(c_pos)
        mc = c.most_common(1)[0]
        if mc[1] > 1:
            ans = 'Crash at {} after {} moves.'.format(mc[0], ct)
            break
    if ans != '':
        print(ans)
        break
    
