# note that this solution is not well-optimized at all and will likely take a
# little while to run

# open the input file and read the contents into a list (list = array in Python)
with open('./inputs/part1-2.txt') as file_input:
    freq_changes = file_input.readlines()

# initialize vars to track where we are in the list, all of the frequencies
# we've already seen, and the cumulative frequency
freq_change_idx = 0
freqs_seen = []
freq_cumulative = 0

# set up an infinite loop -- we'll break the loop once we see our first
# repeated frequency
while True:
    # convert whatever frequency we're at in the list to an integer and
    # add it to the cumulative frequency
    freq_cumulative += int(freq_changes[freq_change_idx].replace('+', ''))
    # if we've already seen this frequency, then we're done and can print
    # this out as our answer!
    if freq_cumulative in freqs_seen:
        print('First reaches {} twice!'.format(freq_cumulative))
        break
    # otherwise, append this to our list of seen frequencies and continue
    freqs_seen.append(freq_cumulative)
    # since part 2 can require iterative over the list multiple times, we
    # need to check our index value -- if we are at the end of the list
    # we reset it to 0 to start the list over again, otherwise we just
    # increment the index by 1 and continue.
    if freq_change_idx == len(freq_changes) - 1:
        freq_change_idx = 0
    else:
        freq_change_idx += 1