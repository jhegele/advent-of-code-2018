# this is just a convenient way to get all the letters in the alphabet
from string import ascii_uppercase

with open('./inputs/part1-2.txt') as puzzle_input:
    sequence = puzzle_input.readlines()[0].strip()

# we need to track the lengths of all the resultant sequences
lens = []
# for each letter in the alphabet
for rem in ascii_uppercase:
    # build a new sequence that excludes any upper or lowercase version
    # of the letter we're working on
    seq2 = [c for c in sequence if c != rem and c != rem.lower()]
    # from here we just build our stack like we did in part 1
    stack = [seq2[0]]
    for char in seq2[1:]:
        if len(stack) == 0:
            stack.append(char)
        else: 
            if stack[-1].swapcase() == char:
                stack.pop()
            else:
                stack.append(char)
    # log the length of this stack
    lens.append(len(stack))

# print the smallest length from all the stacks created
print(min(lens))