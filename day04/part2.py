# NOTE: most of part 2 is an exact duplicate of part 1. comments
# here reflect only those pieces that differ.

import re
from datetime import datetime
from collections import Counter

def parse_entry(val):
    re_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.+)'
    matches = re.search(re_pattern, val)
    return {
        'dt': datetime.strptime(matches.group(1), '%Y-%m-%d %H:%M'),
        'event': matches.group(2).strip()
    }

def parse_event(val):
    if val in ['falls asleep', 'wakes up']:
        return None
    re_pattern = r'Guard #(\d+) begins shift'
    matches = re.search(re_pattern, val)
    return int(matches.group(1))

with open('./inputs/part1-2.txt') as puzzle_input:
    schedule = list(map(parse_entry, puzzle_input.readlines()))

schedule.sort(key=lambda k: k['dt'])
guards = {}
sleep = []
for row in schedule:
    check_guard_id = parse_event(row['event'])
    if check_guard_id is not None:
        guard_id = check_guard_id
        if len(sleep) > 0:
            g, s, e = sleep
            guards[g] + [v for v in range(s, e)]
        if guard_id not in guards:
            guards[guard_id] = []
    else:
        if row['event'] == 'falls asleep':
            sleep = [guard_id, row['dt'].minute, 60]
        if row['event'] == 'wakes up':
            guards[guard_id] += [v for v in range(sleep[1], row['dt'].minute)]
            sleep = []

# part 2 asks us to find the guard that was asleep most often during the same
# minute. to do this, we need a structure that allows us to see the guard id,
# the minute, and how often the guard was asleep during that minute. here we
# are just looping over the guards dict then, for each guard, we build a
# tuple containing the count of times the guard was asleep for the minute (c),
# the minute (m), and the guard id (guard). we again take advantage of the
# fact that python will sort in order of a tuple's contents so, since we have
# c as our first component, that will be the primary sort.
guard_sleep_mins = []
for guard, sleep_mins in guards.items():
    guard_sleep_mins += [(c, m, guard) for m, c in Counter(sleep_mins).items()]

guard_sleep_mins.sort()
# since python sorts in ascending order by default, we take the last element
# from the sorted array (this will be the largest)
min_count, minute, guard_id = guard_sleep_mins[-1]
print('Guard asleep (g): {}'.format(guard_id))
print('Minute asleep (m): {}'.format(minute))
print('Solution (g * m): {}'.format(guard_id * minute))