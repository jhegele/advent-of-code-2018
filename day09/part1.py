# set the number of players
players = 435
# part 1 input
last_marble_played = 71184

# initialize our scoring array and array of marbles
scores = [0 for _ in range(0, players)]
marbles = [0]

# intialize the next marble (m), the next player (p), and the location of the current
# marble (cm)
m = 1
p = 1
cm = 0
# keep looping while we still have marbles to be played
while m <= last_marble_played:
    # if this is a multiple of 23, it's a scoring marble so we need to follow the
    # special instructions around scoring
    if m % 23 == 0:
        # we need the marble 7 away (counter-clockwise) from the current marble, this
        # marble gets added to the score and removed
        score_idx = cm - 7
        # we need to account for situations where moving 7 to the left will take us
        # past index 0
        if score_idx < 0:
            score_idx = len(marbles) + score_idx
        # calculate our score
        scores[p - 1] += m + marbles.pop(score_idx)
        cm = score_idx
    else:
        # if this isn't a scoring marble, we place it two positions away (clockwise)
        # from the current marble
        cm = cm + 2
        # if the new position would take us beyond the length of the array, it'll
        # always loop back around to position 1 in the array
        if cm > len(marbles):
            cm = 1
        # add the marble
        marbles.insert(cm, m)
    # increment the marble and the player
    m += 1
    if p < players:
        p += 1
    else:
        p = 1
    # print(marbles)

# print our answer
print('Max score: {}'.format(max(scores)))