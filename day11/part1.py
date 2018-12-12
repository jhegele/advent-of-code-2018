serial = 3613

# calculate the power level for the cell based on the formula provided in the problem
def power(c, s):
    x, y = c
    p = (((x + 10) * y) + s) * (x + 10)
    p = 0 if p < 100 else int(str(p)[-3])
    return p - 5

# calculate the total power for the 3x3 grid that extends down and to the right from
# the given coordinates (c)
def total_power(c, g, s):
    cells = []
    x, y = c
    for xo in range(0, 3):
        for yo in range(0, 3):
            coords = (x + xo, y + yo)
            if coords in g:
                cells.append(g[coords]['p'])
            else:
                p = power(coords, s)
                cells.append(p)
                g[coords] = {
                    'p': p,
                    'tp': None
                }
                g[coords]['p'] = p
    g[(x, y)]['tp'] = sum(cells)
    return g

# build our grid and calculate the total power at each position
grid = {}
for y in range(1, 299):
    for x in range(1, 299):
        c = (x, y)
        grid = total_power(c, grid, serial)

# find the max total power among all coordinates
max_tp = max([v['tp'] for c, v in grid.items() if v['tp'] is not None])
# get the coordinates associated with the max power
c_max_tp = [c for c, v in grid.items() if v['tp'] == max_tp]
print('Max power is {} at {}'.format(max_tp, c_max_tp))
