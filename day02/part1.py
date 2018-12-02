# import built-in counter -- this will automatically count the occurrences of
# a single entry in a list
from collections import Counter

with open('./inputs/part1-2.txt') as puzzle_input:
    box_ids = puzzle_input.readlines()

# here we are just isolating those ids that have a character that repeats
# either two or three times. inside the set(), we build a list of character
# counts using what is called a list comprehension. basically, we're saying,
# we want to produce a list of v (value) for ever k, v (key, value) combo
# produced by Counter() but ONLY those items where v (value) is equal to 2
# or 3. the map and lambda apply this logic over the entire set of box ids,
# then the list() converts it to a list.
likely_ids = list(map(lambda x: set([v for k, v in Counter(x).items() if v in [2, 3]]), box_ids))

# count the number of 2's in our likely_ids list
occur_2x = len([v for v in likely_ids if 2 in v])
# count the number of 3's in our likely_ids list
occur_3x = len([v for v in likely_ids if 3 in v])

# print our answers
print('Letters that occur two times: {}'.format(occur_2x))
print('Letters that occurr three times: {}'.format(occur_3x))
print('Checksum: {}'.format(occur_2x * occur_3x))