# only commenting where there are differences from part 1
with open('./inputs/parts1-2.txt') as puzzle_input:
    i = [line.strip() for line in puzzle_input.readlines()]

init = i[0].replace('initial state: ', '')
state = {}
for j in range(0, len(init)):
    state[j] = '.' if j < 0 or j >= len(init) else init[j]
patterns = {
    p.split(' => ')[0]: p.split(' => ')[1]
    for p in i[2:]
}

def trim_state(state):
    all_pos = sorted([pos for pos, plant in state.items()])
    all_plant = [state[pos] for pos in all_pos]
    first_plant = all_plant.index('#')
    first_plant_pos = all_pos[first_plant]
    last_plant = len(all_plant) - all_plant[::-1].index('#') - 1
    last_plant_pos = all_pos[last_plant]
    trim = [i for i, v in state.items() if i < first_plant_pos or i > last_plant_pos]
    [state.pop(i) for i in trim]
    return state

def sum_pots(state):
    return sum([i for i, v in state.items() if v == '#'])

# the trick to part 2 is realizing that 50 billion is FAR too many iterations to
# ever actually calculate. if you watch the sums of the pot numbers, it will
# eventually stabilize into a predictable increment each timme. for my input, at
# a certain point, each step is 194 more than the prior step. so, what i did here
# was let the process iterate 1000 times (just to be sure it stabilized) and i
# stored the difference in sum between iteration 900 and 1000. i then averaged
# that list (this is mostly just a check that it's stable -- if this produces a
# fraction, it's not stable yet and you need to iterate beyond 1000). then i
# just use basic math to calculate what the value will be at 50 billion.
last_100_diffs = []
for gen in range(0, 1000):
    all_pos = [pos for pos, plant in state.items()]
    upd = {}
    for pos in range(min(all_pos) - 4, max(all_pos) + 5):
        pat = ''.join([state.get(p, '.') for p in range(pos - 2, pos + 3)])
        upd[pos] = patterns.get(pat, '.')
    for i, v in upd.items():
        state[i] = upd[i]
    state = trim_state(state)
    # here is where we start tracking the final 100 iterations
    if gen >= 900:
        if gen == 900:
            l_sum = sum_pots(state)
        else:
            last_100_diffs.append(sum_pots(state) - l_sum)
            l_sum = sum_pots(state)

# find the average step diff among the last 100 iterations and print it as a
# sanity check
step_diff = sum(last_100_diffs) / len(last_100_diffs)
print('Step diff: {}'.format(step_diff))
# after our 1000 iterations, we need to take this many more steps
remaining_steps = 50000000000 - 1000
# account for the value at 1000 iterations
curr_val = sum_pots(state)
# the remaining steps multiplied by the step difference gives us the added
# value from our remaining iterations (to get to 50 billion). add that to
# the current value and print the result as our answer.
print(remaining_steps * step_diff + curr_val)
