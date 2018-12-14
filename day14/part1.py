puzzle_input = 513401

# initialize our list where we'll keep track of all the scores
scores = ['3', '7']
# recipes is the number of recipes to make before the final n
# recipes (which represents our answer)
recipes = puzzle_input
n = 10

# initialize the worker elves
e1, e2 = 0, 1
# loop until we have at least recipes + n total recipes completed
while len(scores) < recipes + n:
    e1s = int(scores[e1])
    e2s = int(scores[e2])
    # sum the recipe scores and add the result to the end of the 
    # list of scores
    scores.extend((str(e1s + e2s)))
    # update the current recipe that each elf is working on
    e1 = (e1 + 1 + e1s) % len(scores)
    e2 = (e2 + 1 + e2s) % len(scores)

# because it's possible that we added two scores on the last pass
# through the loop the list length could be recipes + n + 1. we
# cut that last value off here if it's present so that we can
# just take the last n value and that will give us our answer.
scores = scores[:(recipes + n)]
print(''.join(scores[-n:]))