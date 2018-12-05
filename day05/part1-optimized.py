# i wanted to optimize this a bit after having some time to think about the
# challenge. rather than parsing the whole string, it's far more efficient
# to use a stack here and build the "reacted" string one letter at a time.
with open('./inputs/part1-2.txt') as puzzle_input:
    sequence = puzzle_input.readlines()[0].strip()

stack = []
# iterate over each character in the input sequence
for char in sequence:
    # if our stack is empty, just add the character
    if len(stack) == 0:
        stack.append(char)
    else: 
        # if the last character in the stack is the opposite case of the
        # current character, remove the last char from the stack and 
        # continue.
        if stack[-1].swapcase() == char:
            stack.pop()
        else:
            stack.append(char)

# the length of the stack gives us our answer
print(len(stack))