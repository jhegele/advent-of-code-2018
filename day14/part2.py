# switched to using a string input here because we need to match this string value
# against the list of scores.
puzzle_input = '513401'

# initialize the list to track scores and create a list from our puzzle input
scores = ['3', '7']
seq = list(puzzle_input)

# init worker elves
e1, e2 = 0, 1
# inifinte loop -- we'll break this as soon as we find our answer
while True:
    # use the logic from P1 to append new recipe scores
    e1s = int(scores[e1])
    e2s = int(scores[e2])
    scores.extend(list(str(e1s + e2s)))
    e1 = (e1 + 1 + e1s) % len(scores)
    e2 = (e2 + 1 + e2s) % len(scores)
    # check to see if the last n characters (where n is the length of our input
    # sequence) matches the input sequence. we also need to check if the n
    # characters ending at the second to last character match. this is, again,
    # because of the situation where we add two scores for a single pass
    # through the loop. if either of these happen, break the loop.
    if scores[-len(seq):] == seq or scores[-len(seq) - 1: -1] == seq:
        if scores[-len(seq) - 1: -1] == seq:
            # if our match ends at the second to last character, trim the last
            # character from the list.
            scores = scores[:len(scores) - 1]
        break
    ct += 1

# our answer is the length of our scores list minus the length of our input sequence
print(len(scores) - len(seq))