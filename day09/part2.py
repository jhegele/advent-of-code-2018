# going to be honest, i wasn't terribly familiar with what a deque structure did but it's
# more-or-less required to solve part 2. i let my part 1 code run for 20+ mins and it
# didn't have a solution. but, using a deque, it runs in just a few seconds.
from collections import deque

players = 435
last_marble_played = 7118400

# initialize our deque with the 0 marble and our scoring array
marbles = deque([0])
scores = [0 for _ in range(0, players)]

# start with player 1
p = 1
# we need to loop through every marble that we need to play
for m in range(1, last_marble_played + 1):
    # if the marble is a multiple of 23, we rotate the deque 7 spaces to the left
    # and remove that element and add it to the score
    if m % 23 == 0:
        marbles.rotate(-7)
        scores[p - 1] += m + marbles.pop()
    else:
        # if this isn't a scoring marble, rotate two positions right (clockwise) and
        # add the marble
        marbles.rotate(2)
        marbles.append(m)
    # next player
    if p == players:
        p = 1
    else:
        p += 1

print(max(scores))