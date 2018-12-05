import re
import sys

# one cycle actually exceeds Python's recursion limit so needed to
# update that limit here to allow it to recurse further
sys.setrecursionlimit(10000)

# from here through importing the puzzle input are unchanged from
# day 1
re_pattern = re.compile(r'(?=([A-Z][a-z]|[a-z][A-Z]))')

def remove(sequence):
    removed = 0
    for match in re.finditer(re_pattern, sequence):
        m = match.group(1)
        if m[0] == m[1].lower() or m[0] == m[1].upper():
            sequence = sequence.replace(m, '')
            removed += 1
    if removed > 0:
        return remove(sequence)
    else:
        return sequence
    

with open('./inputs/part1-2.txt') as puzzle_input:
    sequence = puzzle_input.readlines()[0]

# since part 2 requires removing a single set of units, we need to
# iterate over the alphabet
units = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# this var is where we'll track results for each letter removed
performance = {}
# iterate through the alphabet and remove one letter (upper and lower
# variants) from the raw input string, then run the remove function
# and record the resultant length
for u in units:
    print('Removing {}\{} units...'.format(u, u.lower()))
    modified_sequence = sequence.replace(u, '').replace(u.lower(), '')
    reacted = remove(modified_sequence)
    performance[u] = len(reacted)

# find the shortest string length and print the results
results = [(l, u) for u, l in performance.items()]
results.sort()
best = results[0]
print('Removing unit {}\{} resulted in a length of: {}'.format(best[1], best[1].lower(), best[0]))