import re

# regular expression that will match any capitalized letter followed by
# lowercase or vice versa. this doesn't actually account for whether
# the letters match or not (i.e. this will match Ab and Aa)
re_pattern = re.compile(r'(?=([A-Z][a-z]|[a-z][A-Z]))')

# recursive function that removes all instances of matches based on the
# regex above. this needs to be recursive because removing a match may
# produce another match.
def remove(sequence):
    removed = 0
    # iterate over all matches in the string
    for match in re.finditer(re_pattern, sequence):
        m = match.group(1)
        # here we check whether the matched pattern from the regex is
        # the same letter twice and, if so, remove it from the string
        if m[0] == m[1].lower() or m[0] == m[1].upper():
            sequence = sequence.replace(m, '')
            removed += 1
    # if we removed at least one match, we need to re-run this process
    # because it could have created a new match (ex: AcCa -- removing
    # cC leaves you with Aa which would be a match on the next pass
    # through the string).
    if removed > 0:
        return remove(sequence)
    else:
        return sequence
    
# load puzzle input
with open('./inputs/part1-2.txt') as puzzle_input:
    sequence = puzzle_input.readlines()[0]

# run and print results
fixed_sequence = remove(sequence)
print('Units remaining: {}'.format(len(fixed_sequence)))