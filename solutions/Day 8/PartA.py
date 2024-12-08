from itertools import pairwise

from utils import *
from aocd import get_data, submit

year, day = 2024, 8

dat = get_data(year=year, day=day, block=True)

dat2 = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

dat = Grid(dat)
print(truncate(dat, 80))

tot = 0
antennas = set(dat.values())
antennas_pos = defaultdict(list)
for pos, ant in dat.items():
    if ant == '.':
        continue
    antennas_pos[ant].append(pos)


antis = set()
for ant, positions in antennas_pos.items():
    for ant1, ant2 in combinations(positions, 2):
        diff = sub(ant1, ant2)
        if (apos:=add2(ant1, diff)) in dat:
            antis.add(apos)
        if (apos:=add2(ant2, mul(diff, -1))) in dat:
            antis.add(apos)

tot = len(antis)
print(tot)
submit(tot, part="a", day=day, year=year)
