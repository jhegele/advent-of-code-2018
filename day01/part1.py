# open the input file and read the contents into a list (list = array in Python)
with open('./inputs/part1-2.txt') as file_input:
    freq_changes = file_input.readlines()

# use the map function to convert the strings in our list to integers. we
# want to strip the "+" signs off in order for the string to be accurately
# parsed as an integer. once that is done, we use the sum function to add
# the list up, then print it out as our answer.
print(sum(map(lambda x: int(x.replace('+', '')), freq_changes)))