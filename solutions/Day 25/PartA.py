from utils import *
from aocd import get_data, submit

year, day = 2024, 25

dat = get_data(year=year, day=day, block=True)

dat2 = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''

dat = dat.split('\n\n')

schematics = [Grid(d) for d in dat]
schematics_sets = [set([k for k, v in grid.items() if v == '#']) for grid in schematics]

valid = sum(1 for s1, s2 in combinations(schematics_sets, 2) if len(s1 & s2) == 0)

print(valid)
submit(valid, part="a", day=day, year=year)
