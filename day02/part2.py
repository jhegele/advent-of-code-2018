# since we know that we need to find two strings that are equivalent except
# for a single character, we can test two ids against each other and return
# a 1 for any character than matches and a 0 for any character that doesn't.
# this way, we can sum the list and, if it equals the length of the string
# minus 1, we know we have our match.
def matching_chars(check_id, test_id):
    return sum([1 if val == check_id[idx] else 0 for idx, val in enumerate(test_id)])

with open('./inputs/part1-2.txt') as puzzle_input:
    box_ids = puzzle_input.readlines()

# clean up the ids, they have a new line character at the end after import
box_ids = [v.strip() for v in box_ids]
# iterate over each box id
for idx in range(0, len(box_ids)):
    check_id = box_ids[idx]
    # create a list of all other box ids (this is the list of candidate)
    # matches
    other_ids = [box_id for box_id in box_ids if box_id != check_id]
    # apply our matching function from above to the list of other ids
    other_ids_char_matching = list(map(lambda x: matching_chars(check_id, x), other_ids))
    # in the list of other ids, check to see if there are an elements that are
    # equivalent to the length of the id minus one. if so, we're done.
    if len(check_id) - 1 in other_ids_char_matching:
        match_id = other_ids[other_ids_char_matching.index(len(check_id) - 1)]
        break

# print out our answers
print('Matching box IDs are:')
print(check_id)
print(match_id)
char_matches = [char for idx, char in enumerate(check_id) if char == match_id[idx]]
print('Letters shared: {}'.format(''.join(char_matches)))