import re
import time

re_pattern = re.compile(r'-?\d+')

# parse the digits out of the coordinate line and return them in a dictionary where
# the p element denotes current position (x, y) and v denotes velocity (x, y)
def parse(star):
    m = list(map(int, re_pattern.findall(star)))
    return {
        'p': [m[0], m[1]],
        'v': [m[2], m[3]]
    }

# this function moves the stars positions using their associated velocities. we are
# using a dictionary comprehension to build a new dictionary on the fly from the
# old dictionary
def move(stars):
    return [{
        'p': [s['p'][0] + s['v'][0], s['p'][1] + s['v'][1]],
        'v': s['v']
    } for s in stars]

# draw the stars to the screen
def draw(stars, all_x, all_y):
    # get the position of all stars
    p = [s['p'] for s in stars]
    # find the min and max range so we know how big our board should be. pad by 5
    # to make it easier to see the message
    rx = (min(all_x) - 5, max(all_x) + 5)
    ry = (min(all_y) - 5, max(all_y) + 5)
    # draw the board
    for y in range(ry[0], ry[1]):
        l = []
        for x in range(rx[0], rx[1]):
            c = '.' if [x, y] not in p else '#'
            l.append(c)
        print(' '.join(l))

# import the puzzle inputs
with open('./inputs/part1-2.txt') as puzzle_input:
    stars = list(map(parse, puzzle_input.readlines()))

# count the seconds
ct = 0
while True:
    # get all current x and y values 
    all_x = [s['p'][0] for s in stars]
    all_y = [s['p'][1] for s in stars]
    # here we are finding the range to optimize when we choose to display the
    # message. see below for more info.
    rx = (min(all_x) - 5, max(all_x) + 5)
    ry = (min(all_y) - 5, max(all_y) + 5)
    # we know the message won't be at time = 0 seconds
    if ct > 0:
        # here is where we show our message. as a pure guess, i suspected that
        # the message would be visible when the difference between the min and
        # max x (or y, really) coordinates was at its lowest. i assumed that
        # the distances would decrease over time, reach a minimum where the
        # message would be visible, then begin increasing again. so here we
        # are simply checking to see whether the distance is increasing and,
        # if so, we print out the last second counted and the last position
        # of the stars (not the current position since we've moved them)
        if rx[1] - rx[0] > lrx[1] - lrx[0]:
            # part 2 answer
            print('Seconds elapsed: {}'.format(ct -1))
            # part 1 answer
            draw(ls, all_x, all_y)
            break
    # save values so we can compare them the next time we run through the loop
    lrx, lry, ls = rx, ry, stars
    # move the stars and increase the second count
    stars = move(stars)
    ct += 1