from utils import *
from aocd import get_data, submit

year, day = 2024, 14

dat = get_data(year=year, day=day, block=True)

dat2 = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

dat = parse(dat, ints)
print(truncate(dat, 80))
out = 0

w, h = 101, 103

distinct_tiles = {}
n_elves = len(dat)

for n in range(10_000):
    overlaps = set()
    for px, py, vx, vy in dat:
        px2 = ( px + vx * n ) % w
        py2 = ( py + vy * n ) % h
        overlaps.add((px2, py2))
    distinct_tiles[n] = len(overlaps)

for n, overlap in sorted(distinct_tiles.items(), key=lambda item: item[1])[-10:]:
    print(n, overlap)
    grid = Grid([[' '] * w] * h)
    for px, py, vx, vy in dat:
        px2 = (px + vx * n) % w
        py2 = (py + vy * n) % h
        grid[(px2, py2)] = '#'
    grid.print()
