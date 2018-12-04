import re
from datetime import datetime
from collections import Counter

# function uses regular expressions to parse the components of an input line
def parse_entry(val):
    re_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.+)'
    matches = re.search(re_pattern, val)
    # return a dictionary containing the datetime (dt) and event
    return {
        # the strptime function takes a string and parses it into a python
        # datetime object based on the format provided.
        'dt': datetime.strptime(matches.group(1), '%Y-%m-%d %H:%M'),
        'event': matches.group(2).strip()
    }

# if the row is a guard entry, we need to parse out the guard's id
def parse_event(val):
    # if this is an asleep/awake event, we don't need to worry about
    # this
    if val in ['falls asleep', 'wakes up']:
        return None
    re_pattern = r'Guard #(\d+) begins shift'
    matches = re.search(re_pattern, val)
    return int(matches.group(1))

# import the input, read each line, and convert each line into a parsed
# entry
with open('./inputs/part1-2.txt') as puzzle_input:
    schedule = list(map(parse_entry, puzzle_input.readlines()))

# inputs are out of order, so we need to sort them first
schedule.sort(key=lambda k: k['dt'])
guards = {}
sleep = []
# loop through the rows in our schedule now that it's sorted
for row in schedule:
    # if the row contains a guard id, we need to update which guard
    # we are working with
    check_guard_id = parse_event(row['event'])
    if check_guard_id is not None:
        guard_id = check_guard_id
        # this is here to catch instances where a guard might be asleep
        # at the end of the shift (i.e. where there is a 'falls asleep')
        # event but no corresponding 'wakes up' event). not sure this
        # ever happens but added it just in case.
        if len(sleep) > 0:
            # we're using a list to store attributes of the sleep period
            # so we can use parallel assignment here. parallel assignment
            # is a convenience that allows you to assign multiple vars at
            # the same time.
            g, s, e = sleep
            # add our guard id if we don't already have it
            guards[g] + [v for v in range(s, e)]
        if guard_id not in guards:
            # initialize the guard with an empty list. we'll use this
            # list to track each minute that this guard is sleeping
            guards[guard_id] = []
    # if this row isn't a guard entry, start tracking asleep/awake events
    else:
        if row['event'] == 'falls asleep':
            # i'm initializing this to end at 60 in case there is no
            # corresponding 'wakes up' event. if that were the case
            # we know that the shift ends after an hour so the guard
            # would have slept until min 59
            sleep = [guard_id, row['dt'].minute, 60]
        if row['event'] == 'wakes up':
            # if the guard wakes up, add the minutes slept to the list
            guards[guard_id] += [v for v in range(sleep[1], row['dt'].minute)]
            # reset the sleep var so that nothing gets logged during the
            # guard check
            sleep = []

# build an array of tuples. each tuple will contain the total number of
# minutes the guard was asleep and the guard id. the total number of
# minutes MUST come first in our tuple so that we can take advantage of
# the fact that Python sorts tuples based on the order of their
# contents. in this case, we want to sort by total minutes slept so
# putting that first means that's what Python will sort by first.
guards_mins_asleep = [(len(m), g) for g, m in guards.items()]
guards_mins_asleep.sort()
# python's default sort order is ascending so, to find the largest value
# we need to take the last element of the array.
total_sleep_mins, guard_id_most_mins = guards_mins_asleep[-1]
# now that we have the id of the guard with the most total minutes slept,
# we need to figure out which minute he slept most. use the Counter lib
# to count occurrences of the minute in the list, then sort and pick the
# one with the highest number of occurrences.
c = Counter(guards[guard_id_most_mins])
min_counts = [(c, m) for m, c in c.items()]
min_counts.sort()
occurrences, min_most_asleep = min_counts[-1]
print('Guard most often asleep (g): {}'.format(guard_id_most_mins))
print('Minute most often asleep (m): {}'.format(min_most_asleep))
print('Solution (g * m): {}'.format(guard_id_most_mins * min_most_asleep))