# this is modified from the part 1 solution, comments here are on differences
from collections import Counter

def m_dist(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

def get_total_dist(point, coords):
    # we use a simplified version of the closest() function from part 1.
    # here we only need to calculate the distance to each point, then
    # sum them up.
    distances = list(map(lambda p: m_dist(p, point), coords))
    return sum(distances)

with open('./inputs/part1-2.txt') as puzzle_input:
    coords = puzzle_input.readlines()

coords = [(int(c.split(',')[0].strip()), int(c.split(',')[1].strip())) for c in coords]
coords_x = [c[0] for c in coords]
coords_y = [c[1] for c in coords]
bound_min_x, bound_max_x = min(coords_x), max(coords_x)
bound_min_y, bound_max_y = min(coords_y), max(coords_y)

points = {}
for x in range(bound_min_x, bound_max_x + 1):
    for y in range(bound_min_y, bound_max_y + 1):
        # for each point on the grid, find the total distance to every coordinate
        points[(x, y)] = get_total_dist((x, y), coords)
        
# the problem gives us 10,000 as our upper boundary so find any points where the
# sum of the distance to all coordinates is lower than 10,000. print the length
# of this list as our answer.
valid = [d for p, d in points.items() if d < 10000]
print('Total area size: {}'.format(len(valid)))