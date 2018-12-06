from collections import Counter

# calculate the manhattan distance between two points. since our points
# are tuples, we take the absolute value of the difference between the
# corresponding components of each point.
def m_dist(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

# we need to calculate the distance from each point to each of our
# coordinates.
def get_closest(point, coords):
    # if the point we're looking at is one of our coordinates, just
    # return it since we know that it's the closest (i.e. what we
    # are saying here is that a point is always closest to itself)
    if point in coords:
        return point
    # build a list of the distances to all coordinates
    distances = list(map(lambda p: m_dist(p, point), coords))
    # find the shortest as a list because we need to exclude any
    # points where there is a tie for the shortest
    shortest = [d for d in distances if d == min(distances)]
    if len(shortest) > 1:
        return None
    # return the actual coordinates that are closes
    return coords[distances.index(shortest[0])]

with open('./inputs/part1-2.txt') as puzzle_input:
    coords = puzzle_input.readlines()

# parse our inputs into a list of tuples
coords = [(int(c.split(',')[0].strip()), int(c.split(',')[1].strip())) for c in coords]
# need to find the min/max boundaries for x and y so that we can constrain
# the size of the grid we are working with
coords_x = [c[0] for c in coords]
coords_y = [c[1] for c in coords]
bound_min_x, bound_max_x = min(coords_x), max(coords_x)
bound_min_y, bound_max_y = min(coords_y), max(coords_y)

points = {}
# loop through all points on the grid
for x in range(bound_min_x, bound_max_x + 1):
    for y in range(bound_min_y, bound_max_y + 1):
        # for each point in the grid, get the closest coordinate from
        # our inputs
        closest = get_closest((x, y), coords)
        if closest is not None:
            # we need to check that the closest point doesn't sit on one of our
            # boundaries. any coordinate on a boundary will, by definition, have
            # an area of infinity so it is disqualified for consideration as the
            # closest to a certain point.
            if closest[0] == bound_min_x or closest[0] == bound_max_x or closest[1] == bound_min_y or closest[1] == bound_max_y:
                closest = None
        points[(x, y)] = closest
        
# we want to find the coordinate that is closest to the most points on the grid
# so we need to count the occurences of coordinates across all points. we can
# exclude points where None is the closest.
ct = Counter([c for p, c in points.items() if c is not None])
# print the number of occurrences for the most commonly occurring coordinate
print('Largest area: {}'.format(ct.most_common()[0][1]))