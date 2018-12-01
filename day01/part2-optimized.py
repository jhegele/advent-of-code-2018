# i've attempted to better optimize the part 2 solution here

# import the built-in itertools library. this contains a bunch of utilities
# that are helpful when dealing with iterators (like list or sets)
import itertools

# open the input file and read the contents into a list (list = array in Python)
with open('./inputs/part1-2.txt') as file_input:
    freq_changes = file_input.readlines()

# use the map function to convert our list of inputs from strings to integers
freq_changes = map(int, freq_changes)
# use a set to track what we've seen, sets are much faster than arrays when
# you need to look something up
freqs_seen = set()
# track the cumulative frequency
freq_cumulative = 0

# rather than managing our own loop state, use built-in itertools
for freq in itertools.cycle(freq_changes):
    # if we've seen this cumulative frequency before, we're done!
    if freq_cumulative in freqs_seen:
        print('First reaches {} twice!'.format(freq_cumulative))
        break
    # otherwise add the cumulative freq to the seen list and continue
    freqs_seen.add(freq_cumulative)
    freq_cumulative += freq

# to illustrate the impact of code optimization on performance, this version
# of the solution runs in 0.10 seconds versus 86.60 seconds for the
# non-optimized version
