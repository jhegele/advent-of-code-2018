serial = 3613

# calculate power based on formula in the problem (same as part 1)
def power(c, s):
    x, y = c
    p = (((x + 10) * y) + s) * (x + 10)
    p = 0 if p < 100 else int(str(p)[-3])
    return p - 5

# build the grid of coordinates and associated power
grid = {}
for y in range(1, 301):
    for x in range(1, 301):
        c = (x, y)
        grid[c] = power(c, serial)

# in order to solve this problem efficiently, we need to build a summed-area table. this
# is a data structure where each point contains the sum of values that are above and to
# the left of the point. using this structure, we can quickly solve for a grid of any
# size at any point within the grid.
c_sum = {}
for y in range(1, 301):
    for x in range(1, 301):
        c = (x, y)
        c_sum[c] = grid[c] + c_sum.get((x - 1, y), 0) + c_sum.get((x, y - 1), 0) - c_sum.get((x - 1, y - 1), 0)

# initialize our max to a super low value
max_p = (0, 0, 0, -1e9)
# we need to iterate over every point in the grid, then every possible grid size at that point
for y in range(1, 301):
    for x in range(1, 301):
        for s in range(0, 301 - max(x, y)):
            # here is where we are using some math and our summed area table to calculate
            # the total power for the grid we're looking at. because we want ONLY square
            # grids, we can't simply take the sum of all points above and to the left. we
            # need to start with that, then subtract out the areas that we don't need.
            p = c_sum[(x + s, y + s)] - c_sum[(x + s, y)] - c_sum[(x, y + s)] + c_sum[(x, y)]
            max_p = (x + 1, y + 1, s, p) if p > max_p[3] else max_p

print('{},{},{}'.format(max_p[0], max_p[1], max_p[2]))
