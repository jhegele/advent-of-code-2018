# a lot of this is repeated from part 1
from string import ascii_uppercase

# these vars exist mostly to use the test input which has different params than the
# actual input
base_time_to_comp = 60
total_num_workers = 5

def steps_complete(steps, complete):
    return all(s in complete for s in steps)

with open('./inputs/part1-2.txt') as puzzle_input:
    steps = [line.strip() for line in puzzle_input.readlines()]

steps = [(line.split(' ')[1], line.split(' ')[7]) for line in steps]
dep = {}
all_steps = set()
child_steps = set()
for step in steps:
    p, c = step
    all_steps.add(p)
    all_steps.add(c)
    child_steps.add(c)
    if c not in dep:
        dep[c] = []
    dep[c].append(p)

# build a dict of steps and the time required to complete them
step_lens = {s: base_time_to_comp + ascii_uppercase.index(s) + 1 for s in all_steps}

# reg = our registry where we keep any steps that are ready to be completed
# comp = completed work, work = anything currently being worked on, pick = 
# comprehensive list of steps that have been pickeded up so far.
reg = [s for s in all_steps if s not in child_steps]
comp = []
work = []
pick = []
sec = 0
# keep looping until we're ready to break the loop
while True:
    # move anything that's been worked on for enough time to the completed
    # list, also need to remove those items from the list of work being done
    comp += [s[0] for s in work if s[1] == sec]
    work = [s for s in work if s[1] > sec]
    # if all steps are accounted for in the comp list, we're done
    if len(comp) == len(all_steps):
        break
    # refresh the registry with any steps that are now ready to be completed
    reg += [s for s, p in dep.items() if steps_complete(p, comp) and s not in pick and s not in reg]
    reg.sort(reverse=True)
    # if there are workers that are idle and there is work to be done, assign
    # it
    if len(work) < total_num_workers and len(reg) > 0:
        while len(work) < total_num_workers and len(reg) > 0:
            s = reg.pop()
            work.append((s, sec + step_lens[s]))
            pick.append(s)
    # move to the next seconds
    sec += 1

# print our answer
print(sec)
print(''.join(comp))