# since a step can have multiple parent dependencies, this function tells us if,
# for a given step, all dependencies have been completed
def steps_complete(steps, complete):
    return all(s in complete for s in steps)

# get our puzzle inputs
with open('./inputs/part1-2.txt') as puzzle_input:
    steps = [line.strip() for line in puzzle_input.readlines()]

# parse the letters out of the input line and build a list of tuples where the 
# first element of the tuple is the parent dependency and the second is the
# step
steps = [(line.split()[1], line.split()[7]) for line in steps]
dep = {}
all_steps = set()
child_steps = set()
# set up some helper vars and build a dict where the key is the step and the value
# is the parent dependencies
for step in steps:
    p, c = step
    all_steps.add(p)
    all_steps.add(c)
    child_steps.add(c)
    # here is where we're building our dictionary with the steps and their
    # parent dependencies
    if c not in dep:
        dep[c] = []
    dep[c].append(p)

# initialize our registry -- this is where we'll hold any steps that are ready to
# be started
reg = [s for s in all_steps if s not in child_steps]
# here is where we'll track completed steps in the order they are completed
order = []
# keep iterating as long as we have "stuff" in the registry that needs to be
# completed
while len(reg) > 0:
    # make sure the registry is sorted properly since alphabetical order is the
    # tiebreaker
    reg.sort(reverse=True)
    # grab the task from the end of the registry and put it in the order var
    order.append(reg.pop())
    # update the registry with any tasks that are ready now that we've
    # completed new tasks
    reg += [s for s, p in dep.items() if steps_complete(p, order) and s not in order and s not in reg]

# print the answer
print(''.join(order))