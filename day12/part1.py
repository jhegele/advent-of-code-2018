with open('./inputs/parts1-2.txt') as puzzle_input:
    i = [line.strip() for line in puzzle_input.readlines()]

# this is just formatting our inputs into useable structures
init = i[0].replace('initial state: ', '')
state = {}
for j in range(0, len(init)):
    state[j] = '.' if j < 0 or j >= len(init) else init[j]
patterns = {
    p.split(' => ')[0]: p.split(' => ')[1]
    for p in i[2:]
}

# this function trims off any excess elements from the beginning and
# ending of the state. this isn't necessary but it helps us avoid
# a situation where we have a huge string of periods (.) before and
# after the actual start of the state.
def trim_state(state):
    all_pos = [pos for pos, plant in state.items()]
    all_plant = [plant for pos, plant in state.items()]
    first_plant = all_plant.index('#')
    last_plant = len(all_plant) - all_plant[::-1].index('#') - 1
    trim = []
    for i, v in state.items():
        if i < all_pos[first_plant] - 4 or i > all_pos[last_plant] + 4:
            trim.append(i)
    [state.pop(i) for i in trim]
    return state

# get the sum of the pot numbers where a plant exists
def sum_pots(state):
    return sum([i for i, v in state.items() if v == '#'])

# loop through 20 generations
for gen in range(0, 20):
    # get all current pot positions from the state
    all_pos = [pos for pos, plant in state.items()]
    # we need to make all updates at the same time (rather than sequentially
    # as they happen) in order to avoid pattern matching issues. this var
    # is where we'll track our updates.
    upd = {}
    # we need to start 4 spots before the first position in our state. this
    # is because the patterns we're looking for are 5 characters long so
    # it's possible that the first character will trigger a plant in a pot
    # that exists before the start of our current state. similarly we need
    # to extend 4 characters beyond the end of our state.
    for pos in range(min(all_pos) - 4, max(all_pos) + 5):
        # get the pattern of the surrounding cells
        pat = ''.join([state.get(p, '.') for p in range(pos - 2, pos + 3)])
        # if we have a match in the patterns from our input, update 
        # accordingly. if there is no match, this position has no plant in
        # the next generation
        upd[pos] = patterns.get(pat, '.')
    for i, v in upd.items():
        state[i] = upd[i]

# print the sum of the pots in the final state as our answer
print(sum_pots(state))
